from fastapi.testclient import TestClient

from app.main import app


def test_component_predict_reads_user_from_file_and_predicts(tmp_path):
    p = tmp_path / "users.txt"
    p.write_text("userA\nuserB\n", encoding="utf-8")

    client = TestClient(app)

    user_id = p.read_text(encoding="utf-8").splitlines()[0]
    resp = client.post(
        "/predict",
        json={
            "user_id": user_id,
            "num_buckets": 1000,
        },
    )

    assert resp.status_code == 200
    data = resp.json()

    assert "bucket" in data and "prediction" in data
    assert 0 <= data["bucket"] < 1000
    assert data["prediction"] in (0, 1)
