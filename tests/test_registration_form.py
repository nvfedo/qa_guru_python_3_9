from demoqa_tests.model.data.users import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm
from allure_commons.types import Severity
import allure


@allure.tag('WEB')
@allure.label('owner', 'nvfedo')
@allure.severity(Severity.CRITICAL)
@allure.feature('Practice form')
@allure.story('User register')
@allure.title('Successful register with all fields are filled')
def test_registration_user_with_all_fields(setup_chrome):
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
    with allure.step('Fill form'):
        practice_form.fill_form(test_user)
    with allure.step('Validate form'):
        practice_form.should_have_filled()


@allure.tag('WEB')
@allure.label('owner', 'nvfedo')
@allure.severity(Severity.CRITICAL)
@allure.feature('Practice form')
@allure.story('User register')
@allure.title('Successful register with only required fields are filled')
def test_registration_user_with_only_required_fields(setup_chrome):
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
    with allure.step('Fill only required fields'):
        practice_form.open_page()
        practice_form.fill_name(test_user)
        practice_form.select_gender(test_user)
        practice_form.fill_contacts(test_user)
        practice_form.select_birthday(test_user)


@allure.tag('WEB')
@allure.label('owner', 'nvfedo')
@allure.severity(Severity.MINOR)
@allure.feature('Practice form')
@allure.story('User register')
@allure.title('Failed registration without filling out forms')
def test_registration_user_with_empty_fields(setup_chrome):
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
    with allure.step('Do not fill any fields and submit'):
        practice_form.open_page()
        practice_form.submit()
    with allure.step('Validating empty fields'):
        practice_form.validating_an_empty_phone_field()
        practice_form.validating_an_empty_first_name_field()
        practice_form.validating_an_empty_last_name_field()


@allure.tag('WEB')
@allure.label('owner', 'nvfedo')
@allure.severity(Severity.MINOR)
@allure.feature('Practice form')
@allure.story('User register')
@allure.title('Failed registration with incorrect number')
def test_registration_user_with_incorrect_number(setup_chrome):
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
    with allure.step('Fill all required field, except phone number'):
        practice_form.open_page()
        practice_form.fill_name(test_user)
        practice_form.select_gender(test_user)
        practice_form.select_birthday(test_user)
        practice_form.submit()
    with allure.step('Validating incorrect phone number field'):
        practice_form.validating_an_empty_phone_field()
