import sys

sys.path.append("..")
for path in sys.path:
    print(path)

from MWWC_ContactSyncTool.app import index


def test_index():
    data = index()
    assert "The UI goes here." in data
