import pytest
from models.users import User
from pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page():
    return RegistrationPage()


@pytest.fixture
def user():
    return User("John", "Doe", "gte@mail.com", "Male", "1234567890",
                "7 August,2023", ["English", "Math"], ["Sports", "Music"],
                "pic.jpeg", "123 Main St, Haryana Karnal")


class TestFillForm:
    def test_success_fill_form(self, registration_page, user):
        registration_page.open()
        registration_page.register(user)
        registration_page.should_have_registered(user)
