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

        registration_page.fill_first_name(user.first_name)
        registration_page.fill_last_name(user.last_name)
        registration_page.fill_email(user.email)
        registration_page.choose_gender(user.gender)
        registration_page.fill_phone(user.phone_number)
        registration_page.choose_date_of_birth(user.date_of_birth)
        registration_page.fill_subjects(user.subjects)
        registration_page.choose_hobbies(user.hobbies)
        registration_page.upload_picture(user.picture)
        registration_page.fill_address(user.address)

        registration_page.submit()

        registration_page.should_have_registered(user)
