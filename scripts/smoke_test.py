import time

import requests


def main() -> int:
    url = "http://localhost:8000/health"

    for _ in range(20):
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                print("Smoke test PASSED ✅")
                print(r.text)
                return 0
        except requests.RequestException:
            time.sleep(0.5)

    print("Smoke test FAILED ❌ (service not reachable on localhost:8000)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
