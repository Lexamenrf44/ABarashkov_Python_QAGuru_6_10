from selene import have

from src.pages.app import RegistrationPage


def test_fill_check_practice_form():

    registration_page = RegistrationPage()

    # Should open page
    registration_page.open()
    (
        # Should fill elements
        registration_page
        .script_trick()
        .fill_first_name('Alex')
        .fill_last_name('Barashka')
        .fill_email('abarashka@gmail.com')
        .fill_gender('Male')
        .fill_phone_number('1234567890')
        .fill_date_of_birth('1', 'December', '1998')
        .fill_hobbies('Sports')
        .fill_subject('Computer Science')
        .upload_image('chatgpt_logo.png')
        .fill_current_address('Tbilisi')
        .fill_state('NCR')
        .fill_city('Delhi')
    )

    registration_page.submit()

    registration_page.should_registered_user_with.should(
        have.exact_texts(
            'Alex Barashka',
            'abarashka@gmail.com',
            'Male',
            '1234567890',
            '01 December,1998',
            'Computer Science',
            'Sports',
            'chatgpt_logo.png',
            'Tbilisi',
            'NCR Delhi'
        )

    )
