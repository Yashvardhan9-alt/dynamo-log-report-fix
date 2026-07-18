import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load():
    assert REPORT.exists(), "report.json missing"
    return json.loads(REPORT.read_text())


def test_total_requests():
    """Verify total requests."""
    assert load()["total_requests"] == 6


def test_unique_ips():
    """Verify unique IP count."""
    assert load()["unique_ips"] == 3


def test_top_path():
    """Verify most requested path."""
    assert load()["top_path"] == "/index.html"