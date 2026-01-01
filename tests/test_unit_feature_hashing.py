import pytest

from app.feature_engineering import hashed_feature


def test_hashed_feature_is_deterministic():
    a = hashed_feature("known_user", 1000)
    b = hashed_feature("known_user", 1000)
    assert a == b


def test_hashed_feature_bucket_range():
    x = hashed_feature("any", 50)
    assert 0 <= x < 50


def test_hashed_feature_known_value_regression():
    expected = hashed_feature("mlops", 1000)
    assert hashed_feature("mlops", 1000) == expected


def test_invalid_num_buckets():
    with pytest.raises(ValueError):
        hashed_feature("x", 0)