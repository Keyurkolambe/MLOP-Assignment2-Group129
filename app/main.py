import time
import logging
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
from app.model_loader import load_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("cats-dogs-api")

app = FastAPI(title="Cats vs Dogs API")

REQUEST_COUNT = 0

@app.get("/health")
def health():
    return {"status": "ok", "version" : "v3"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    global REQUEST_COUNT
    REQUEST_COUNT += 1

    start = time.time()

    img = Image.open(file.file).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    model = load_model()
    prob_dog = float(model.predict(arr)[0][0])
    prob_cat = 1.0 - prob_dog

    label = "dog" if prob_dog > 0.5 else "cat"
    latency_ms = (time.time() - start) * 1000

    logger.info(
        f"request={REQUEST_COUNT} file={file.filename} label={label} "
        f"prob_dog={prob_dog:.4f} latency_ms={latency_ms:.2f}"
    )

    return {
        "label": label,
        "probabilities": {
            "cat": prob_cat,
            "dog": prob_dog
        },
        "latency_ms": latency_ms,
        "request_count": REQUEST_COUNT
    }
