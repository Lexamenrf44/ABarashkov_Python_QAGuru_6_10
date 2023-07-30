from selene import browser, have, command, be

from src.conftest import path


class RegistrationPage:

    def __init__(self):
        self.should_registered_user_with = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form')

    def script_trick(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
        return self

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('[class="react-datepicker__year-select"]').type(year)
        browser.element(f'.react-datepicker__day--00{day}').click()
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def fill_hobbies(self, hobby):
        browser.all('[for^= hobbies]').element_by(have.text(hobby)).element('..').click()

        return self

    def upload_image(self, file_name):
        browser.element('#uploadPicture').send_keys(path(file_name))

        return self

    def fill_current_address(self, value):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#currentAddress').should(be.blank).type(value)

        return self

    def fill_state(self, state):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(state)).click()

        return self

    def fill_city(self, city):
        browser.element('#city').click()
        browser.all("[id^=react-select][id*=option]").element_by(have.exact_text(city)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)
