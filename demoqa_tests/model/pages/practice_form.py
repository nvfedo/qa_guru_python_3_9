from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.radiobutton import Radio
from demoqa_tests.model.data.users import User
from demoqa_tests.utils import file_path, datetime_config


class PracticeForm:
    def __init__(self, user: User):
        self.user = user

    def open_page(self):
        browser.open('https://demoqa.com/automation-practice-form/')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def fill_name(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        return self

    def fill_contacts(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.phone)
        return self

    def select_gender(self, user):
        gender = Radio(browser.all('[name=gender]'))
        gender.select_by_value(user.gender)
        return self

    def select_birthday(self, user):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(user.birthday)
        return self

    def input_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def select_hobbies(self, user):
        check_hobbies = Checkbox(browser.all('[for^=hobbies-checkbox]'))
        check_hobbies.select(user.hobbies)
        return self

    def upload_image(self):
        relative_path = 'resources/photo.jpg'
        path = file_path.create_path(relative_path)
        browser.element('#uploadPicture').set_value(path)
        return self

    def input_address(self, user):
        browser.element('#currentAddress').type(user.address)
        return self

    def select_state(self, user):
        dropdown = Dropdown('#state')
        dropdown.select(user.state)
        return self

    def select_city(self, user):
        dropdown = Dropdown('#city')
        dropdown.select(user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def scroll_to_bottom(self):
        browser.element('#state').perform(command.js.scroll_into_view)
        return self

    def fill_form(self, user):
        self.open_page()
        self.fill_name(user)
        self.fill_contacts(user)
        self.select_gender(user)
        self.select_birthday(user)
        self.input_subject(user)
        self.select_hobbies(user)
        self.upload_image()
        self.input_address(user)
        self.scroll_to_bottom()
        self.select_state(user)
        self.select_city(user)
        self.submit()

    def should_have_filled(self):
        browser.element('.table').all('td').even.should(have.texts(
            self.user.first_name + ' ' + self.user.last_name,
            self.user.email,
            self.user.gender,
            self.user.phone,
            self.user.birthday.strftime(datetime_config.datetime_view_format),
            self.user.subject,
            self.user.hobbies,
            self.user.image,
            self.user.address,
            self.user.state + ' ' + self.user.city))

    def validating_an_empty_phone_field(self):
        browser.element('#userNumber').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self

    def validating_an_empty_first_name_field(self):
        browser.element('#firstName').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self

    def validating_an_empty_last_name_field(self):
        browser.element('#lastName').should(have.css_property('border-color', value='rgb(220, 53, 69)'))
        return self
