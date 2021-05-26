from pathlib import Path

from project.app import app, init_db


def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="application/json")

    assert response.status_code == 200
    #assert response.data == b"Hello, World!"


def test_database():
    init_db()
    assert Path("horus.db").is_file()