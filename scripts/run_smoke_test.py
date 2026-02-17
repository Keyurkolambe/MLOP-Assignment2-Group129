import time
import requests

BASE_URL = "http://127.0.0.1:8000"
IMAGE_PATH = "assets/38.jpg"

def wait_for_api(timeout_sec=90):
    start = time.time()
    while time.time() - start < timeout_sec:
        try:
            r = requests.get(f"{BASE_URL}/health", timeout=5)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(2)
    return False

def main():
    ok = wait_for_api(90)
    if not ok:
        raise RuntimeError("API did not become ready")

    r = requests.get(f"{BASE_URL}/health", timeout=10)
    r.raise_for_status()

    with open(IMAGE_PATH, "rb") as f:
        r = requests.post(f"{BASE_URL}/predict", files={"file": f}, timeout=30)
    r.raise_for_status()

    print("Smoke test passed")

if __name__ == "__main__":
    main()
