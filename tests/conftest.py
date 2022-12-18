import pytest
from api.models import Account
from api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    account = Account('Test Account', '€')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()