import pytest
import json
from pathlib import Path

from project.server import app, init_db

def test_database():
    """" Ensure DB exists """
    init_db()
    assert Path("app.db").is_file()

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="application/json")
    assert response.status_code == 200

def test_add_new_contact():
    """" Creates new contact and check returned status """
    tester = app.test_client()
    response = tester.post("/new/?contact_name=test&contact_phone=0101010101987654321", content_type="application/json", follow_redirects=True)
    json_data = json.loads(response.data)
    assert response.status_code == 200
    assert 'status' in json_data 
    assert json_data['status'] == 1

def test_remove_same_contact():
    """" Recover contacts list and remove previously added contact """
    tester = app.test_client()
    response = tester.get("/", content_type="application/json")
    json_data = json.loads(response.data)
    assert response.status_code == 200
    found = False
    for contact in json_data['json_list']:
        print(contact)
        if contact['contact_name'] == 'test':
            found = True
            del_response = tester.get("/update/"+str(contact['id'])+"?method=delete", content_type="application/json")
            delete_json = json.loads(del_response.data)
            assert del_response.status_code == 200
            assert delete_json['status'] == 1
    assert found

    