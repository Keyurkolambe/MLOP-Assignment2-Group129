# 🐱🐶 Cats vs Dogs – End-to-End MLOps Pipeline

This project implements a complete end-to-end **MLOps pipeline** for binary image classification (Cats vs Dogs) for a pet adoption platform.

It includes:

- Data versioning using DVC  
- Model training and experiment tracking using MLflow  
- REST API inference service using FastAPI  
- Docker containerization  
- Continuous Integration (CI)  
- Continuous Deployment (CD)  
- Basic monitoring and logging  

---

# 📁 Project Structure

```
cats-dogs-mlops/
│
├── .dvc/
├── .github/workflows/ci-cd.yml
├── app/
├── assets/
├── data/
├── eval_samples/
├── models/
├── notebooks/
├── scripts/
├── src/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .gitignore
└── .dvcignore
```

---

# 🚀 1. Local Setup Instructions

## Clone Repository

```bash
git clone <repository_url>
cd cats-dogs-mlops
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 2. Dataset Versioning (DVC)

Initialize DVC:

```bash
dvc init
```

Track raw dataset:

```bash
dvc add data/raw
```

Track processed dataset:

```bash
dvc add data/processed
```

Commit DVC files:

```bash
git add .
git commit -m "Track datasets with DVC"
```

If using remote:

```bash
dvc push
```

On another machine:

```bash
dvc pull
```

---

# 🧠 3. Model Development & Experiment Tracking (M1)

## Preprocessing
Notebook:
```
notebooks/01_preprocess.ipynb
```

- Resize images to 224×224 RGB
- Split dataset into 80/10/10 (train/val/test)
- Save to `data/processed/`

## Training
Notebook:
```
notebooks/02_train_with_mlflow.ipynb
```

- Train baseline CNN model
- Apply data augmentation
- Save model to:
```
models/cats_dogs_model.h5
```

## MLflow

Start MLflow UI:

```bash
mlflow ui
```

Open in browser:

```
http://127.0.0.1:5000
```

Tracked:
- Parameters
- Metrics
- Confusion matrix
- Training curves
- Model artifact

---

# 🌐 4. Inference Service (M2)

FastAPI application:

```
app/main.py
```

### Endpoints

**Health Check**
```
GET /health
```

**Prediction**
```
POST /predict
```

Returns:
- Predicted label (cat/dog)
- Class probabilities
- Latency
- Request count

Run locally:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 🐳 5. Docker Containerization (M2)

Build Docker image:

```bash
docker build -t cats-dogs-api .
```

Run container:

```bash
docker run -p 8000:8000 cats-dogs-api
```

Test health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

---

# 🔁 6. Continuous Integration (CI) – M3

CI is implemented using **GitHub Actions**.

Configuration file:

```
.github/workflows/ci-cd.yml
```

On every push to `main` branch, CI performs:

- Checkout repository
- Setup Python environment
- Install dependencies
- Run unit tests (`pytest`)
- Build Docker image

CI ensures:
- Code correctness
- Test validation
- Successful Docker build

---

# 🚀 7. Continuous Deployment (CD) – M4

CD handles automatic deployment of the containerized service.

Deployment files:

- `Dockerfile`
- `docker-compose.yml`

CD process:

- Pull latest Docker image
- Deploy/update service using docker-compose
- Perform health check validation
- Validate `/predict` endpoint (smoke test)

Deploy using:

```bash
docker-compose up --build
```

Stop deployment:

```bash
docker-compose down
```

---

# 📊 8. Monitoring & Logging (M5)

Logging implemented in:

```
app/main.py
```

Tracks:
- Request count
- Prediction label
- Prediction probability
- Latency per request

View container logs:

```bash
docker logs <container_id>
```

---

# 🔄 9. Reproducing on a New Machine

1. Clone repository  
2. Create virtual environment  
3. Install dependencies  
4. Run `dvc pull` (if remote configured)  
5. Build Docker image  
6. Deploy using docker-compose  
7. Verify health and prediction endpoints  

---

# 🎯 Deliverables

- Source code with DVC, CI/CD, Docker, deployment configuration
- Trained model artifact
- Screen recording demonstrating full MLOps workflow
