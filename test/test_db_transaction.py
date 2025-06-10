from database.db_transaction import DBTransaction
from database.table import Table
from model import User

from datetime import datetime
import pytest


@pytest.fixture(scope="module")
def db():
    db_transaction = DBTransaction()
    yield db_transaction
    db_transaction.conn.execute("DELETE FROM users;")  # tabloyu temizle
    db_transaction.conn.commit()
    db_transaction.conn.close()
    
def test_add_and_get_user(db):
    user = User(
        name="Jane Doe",
        email="jane@example.com",
        birthdate=datetime.strptime("1990-01-01", "%Y-%m-%d"),
        password="jane123",
        priority=0,
        id_number=12345678
    )
    db.add_new_entity(Table.USER, user)

    fetched = db.get_entity(Table.USER, {"email": "jane@example.com"})
    assert fetched.name == "Jane Doe"
    assert fetched.email == user.email

def test_get_entities_with_filter(db):
    results = db.get_entities(Table.USER, ("priority", "=", 0))
    assert len(results) >= 1
    assert any(user.email == "jane@example.com" for user in results)

def test_update_user(db):
    car = db.get_entity(Table.CAR, {"entity_id": "1a2b3c4d-aaaa-1111-bbbb-1234567890ab"})
    assert car != None
    car.gas_type = "gasoline"
    db.update_entity(Table.CAR, car)
    updated = db.get_entity(Table.CAR, {"entity_id": "1a2b3c4d-aaaa-1111-bbbb-1234567890ab"})
    assert updated.gas_type == "gasoline"

def test_delete_user(db):
    user = db.get_entity(Table.USER, {"email":"jane@example.com"})
    db.delete_entity(Table.USER, user.entity_id)
    deleted = db.get_entity(Table.USER, {"email": "jane@example.com"})
    assert deleted is None
