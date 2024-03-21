from typing import Generator
import pytest
from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@gmail.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test_password"
}

@pytest.fixture
def user(db) -> Generator[User, None, None]:
    user = User.objects.create_user(**data_user)
    yield user
