import sys

sys.path.append("..")

from src.app import index


def test_index():
    data = index()
    assert "The UI goes here." in data
