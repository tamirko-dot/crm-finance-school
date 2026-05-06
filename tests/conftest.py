import pytest
from django.test import Client

from accounts.models import User, UserRole


@pytest.fixture
def client():
    return Client()


def make_user(email: str, role: str, password: str = "Test1234!") -> User:
    user = User.objects.create_user(
        email=email,
        username=email.split("@")[0],
        password=password,
        role=role,
        full_name_he=f"Test {role}",
    )
    return user


@pytest.fixture
def trainee(db):
    return make_user("trainee@test.local", UserRole.TRAINEE)


@pytest.fixture
def manager(db):
    return make_user("manager@test.local", UserRole.CUSTOMER_MANAGER)


@pytest.fixture
def admin_user(db):
    u = make_user("admin@test.local", UserRole.ADMIN)
    u.is_staff = True
    u.save()
    return u


@pytest.fixture
def ceo(db):
    return make_user("ceo@test.local", UserRole.CEO)
