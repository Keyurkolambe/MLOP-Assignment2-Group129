import requests

BASE_URL = "http://127.0.0.1:8000"
IMAGE_PATH = "assets/38.jpg"

def test_health():
    r = requests.get(f"{BASE_URL}/health", timeout=10)
    r.raise_for_status()
    data = r.json()
    assert data.get("status") == "ok"
    print("Health OK")

def test_predict():
    with open(IMAGE_PATH, "rb") as f:
        r = requests.post(
            f"{BASE_URL}/predict",
            files={"file": f},
            timeout=30
        )
    r.raise_for_status()
    data = r.json()

    assert "label" in data
    assert "probabilities" in data
    assert "cat" in data["probabilities"]
    assert "dog" in data["probabilities"]

    print("Predict OK:", data["label"], data["probabilities"])

def main():
    test_health()
    test_predict()
    print("Smoke test passed")

if __name__ == "__main__":
    main()
