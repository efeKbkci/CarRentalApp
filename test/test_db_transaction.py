import pytest
import os
import sqlite3
from database.db_transaction import DBTransaction
from database.table import Table
from model import User
from datetime import datetime
from dataclasses import asdict

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
    db.add_new_entity(Table.USER, asdict(user))

    fetched = db.get_entity(Table.USER, {"email": "jane@example.com"})
    assert fetched.name == "Jane Doe"
    assert fetched.email == user.email

def test_get_entities_with_filter(db):
    results = db.get_entities(Table.USER, [("priority", "=", 0)])
    assert len(results) >= 1
    assert any(user.email == "jane@example.com" for user in results)

def test_update_user(db):
    user = db.get_entity(Table.USER, {"email":"jane@example.com"})
    assert user != None
    db.update_entity(Table.USER, user.entity_id, {"name": "Jane Updated"})
    updated = db.get_entity(Table.USER, {"email": "jane@example.com"})
    assert updated.name == "Jane Updated"

def test_delete_user(db):
    user = db.get_entity(Table.USER, {"email":"jane@example.com"})
    db.delete_entity(Table.USER, user.entity_id)
    deleted = db.get_entity(Table.USER, {"email": "jane@example.com"})
    assert deleted is None
