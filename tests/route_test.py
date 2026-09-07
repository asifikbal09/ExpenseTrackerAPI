from uuid import UUID

from tests.conftest import TEST_USER_ID


def test_create_transaction(client):
    payload = {
        "title": "Lunch",
        "amount": 250,
        "type": "expense",
        "category": "Food",
    }

    response = client.post("/transactions/", json=payload)

    print("\nSTATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 201


def test_get_transactions(client):
    payload = {
        "title": "Lunch",
        "amount": 250,
        "type": "expense",
        "category": "Food",
    }

    create_response = client.post(
        "/transactions/",
        json=payload,
    )

    assert create_response.status_code == 201

    response = client.get("/transactions/")

    print("\nGET ALL STATUS:", response.status_code)
    print("GET ALL RESPONSE:", response.json())

    assert response.status_code == 200


def test_get_transaction_by_id(client):
    payload = {
        "title": "Dinner",
        "amount": 500,
        "type": "expense",
        "category": "Food",
    }

    create_response = client.post(
        "/transactions/",
        json=payload,
    )

    assert create_response.status_code == 201

    transaction = create_response.json()["data"]
    transaction_id = transaction["id"]

    response = client.get(
        f"/transactions/{transaction_id}"
    )

    assert response.status_code == 200

    data = response.json()["data"]

    assert data["id"] == transaction_id
    assert data["title"] == "Dinner"
    assert data["amount"] == 500


def test_update_transaction(client):
    create_payload = {
        "title": "Old Title",
        "amount": 300,
        "type": "expense",
        "category": "Food",
    }

    create_response = client.post(
        "/transactions/",
        json=create_payload,
    )

    assert create_response.status_code == 201

    transaction = create_response.json()["data"]
    transaction_id = transaction["id"]

    update_payload = {
        "title": "Updated Title",
        "amount": 450,
    }

    response = client.put(
        f"/transactions/{transaction_id}",
        json=update_payload,
    )

    assert response.status_code == 200

    data = response.json()["data"]

    assert data["id"] == transaction_id
    assert data["title"] == "Updated Title"
    assert data["amount"] == 450

    assert data["type"] == "expense"
    assert data["category"] == "Food"

def test_delete_transaction(client):
    create_payload = {
        "title": "Delete Me",
        "amount": 100,
        "type": "expense",
        "category": "Test",
    }

    create_response = client.post(
        "/transactions/",
        json=create_payload,
    )

    assert create_response.status_code == 201

    transaction = create_response.json()["data"]
    transaction_id = transaction["id"]

    response = client.delete(
        f"/transactions/{transaction_id}"
    )

    assert response.status_code == 200

    data = response.json()["data"]

    assert data["id"] == transaction_id
    assert data["title"] == "Delete Me"