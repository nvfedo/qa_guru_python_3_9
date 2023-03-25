from demoqa_tests.model.data.users import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm


def test_registration_user():
    practice_form = PracticeForm(test_user)
    practice_form.submit_form()
    practice_form.should_have_submitted()
