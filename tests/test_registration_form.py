from time import sleep

from demoqa_tests.model.data.users import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm
from allure_commons.types import Severity
import allure


@allure.tag('WEB')
@allure.label('owner', 'nvfedo')
@allure.severity(Severity.CRITICAL)
@allure.feature('Practice form')
@allure.description('Checking all fields are filled')
@allure.story('User register')
@allure.title("Successful register user")
def test_registration_user(setup_chrome):
    with allure.step('Open practice form'):
        practice_form = PracticeForm(test_user)
        sleep(1)
    with allure.step('Submit form'):
        practice_form.submit_form()
        sleep(1)
    with allure.step('Validate form'):
        practice_form.should_have_submitted()
        sleep(1)
