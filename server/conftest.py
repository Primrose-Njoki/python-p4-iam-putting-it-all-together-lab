import pytest
from app import app, db

@pytest.fixture(autouse=True, scope='session')
def setup_database():
    with app.app_context():
        db.create_all()
