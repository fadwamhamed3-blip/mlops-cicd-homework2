from dataclasses import dataclass

@dataclass
class DummyModel:
    threshold: int = 500

    def predict(self, bucket_index: int) -> int:
        return 1 if bucket_index >= self.threshold else 0
