import os
import random
import requests

BASE_URL = "http://127.0.0.1:8000"
TEST_DIR = "data/processed/test"
SAMPLES_PER_CLASS = 20

def list_images(folder):
    return [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

def main():
    cats = list_images(os.path.join(TEST_DIR, "cats"))
    dogs = list_images(os.path.join(TEST_DIR, "dogs"))

    random.shuffle(cats)
    random.shuffle(dogs)

    samples = [(p, "cat") for p in cats[:SAMPLES_PER_CLASS]] + [(p, "dog") for p in dogs[:SAMPLES_PER_CLASS]]
    random.shuffle(samples)

    correct = 0

    for path, true_label in samples:
        with open(path, "rb") as f:
            r = requests.post(f"{BASE_URL}/predict", files={"file": f}, timeout=30)
        r.raise_for_status()
        pred = r.json()["label"]

        if pred == true_label:
            correct += 1

    total = len(samples)
    acc = correct / total

    print("Total samples:", total)
    print("Correct:", correct)
    print("Accuracy:", acc)

if __name__ == "__main__":
    main()
