import pytest
import json
from pathlib import Path

from project.server import app, init_db


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="application/json")

    assert response.status_code == 200
    #assert response.data == b"Hello, World!"


def test_database():
    init_db()
    assert Path("project/app.db").is_file()