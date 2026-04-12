import sys
import pytest


def pytest_collection_modifyitems(items):
    if sys.platform != "win32":
        skip_win = pytest.mark.skip(reason="Requires Windows")
        for item in items:
            if "test_mcp" in item.nodeid:
                item.add_marker(skip_win)
