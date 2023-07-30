import datetime

from selene import have
from src.pages.app import RegistrationPage
from src.models.data import User


def test_fill_check_practice_form():
    registration_page = RegistrationPage()

    sasha = User(
        first_name='Alex',
        last_name='Barashka',
        email='abarashka@gmail.com',
        gender='Male',
        phone_number='1234567890',
        date_of_birth=datetime.date(1998, 12, 1),
        hobbies='Sports',
        subjects='Computer Science',
        image='chatgpt_logo.png',
        current_address='Tbilisi',
        state='NCR',
        city='Delhi'

    )
    registration_page.open()
    registration_page.script_trick()
    registration_page.register(sasha)
    registration_page.should_have_registered(sasha)
