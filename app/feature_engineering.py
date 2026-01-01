import hashlib


def hashed_feature(value: str, num_buckets: int = 1000) -> int:
    if num_buckets <= 0:
        raise ValueError("num_buckets must be > 0")

    if value is None:
        value = ""

    h = hashlib.sha256(value.encode("utf-8")).hexdigest()
    as_int = int(h, 16)
    return as_int % num_buckets
