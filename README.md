<h2 align="center">Autotest UI project for demoqa.com</h2>

### Stack and tools
<p  align="center">
  <code><img width="5%" title="Pycharm" src="attach/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="attach/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="attach/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="attach/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="attach/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="attach/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="attach/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="attach/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="attach/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="attach/logo/telegram.png"></code>
</p>

### What does the test do:
- [x] Fills in the fields of the registration form. Elements such as checkbox, datepicker, dropdown, radiobutton and others are used
- [x] Submit filled fields
- [x] Validation filled fields

### <img width="3%" title="Jenkins" src="attach/logo/jenkins.png"> Project in Jenkins

### [Job](https://jenkins.autotests.cloud/job/nvfedo_UI_tests_demoqa/)

#### Just click "Build Now" and the tests will start building and passing them through the virtual machine
![Screen](attach/screenshots/jenkins_main.png)

### <img width="3%" title="Allure Report" src="attach/logo/allure_report.png"> Allure report

#### After passing the tests, the results are recorded in the Allure report. Tests have attachments such as screenshot, video, page_source and browser log.
![Screen](attach/screenshots/allure_report.png)

#### Test video
![Screen](attach/video/fill_practice_form.gif)

### ![Screen]("attach/logo/allure_testops.png") Integration with Allure TestOps is also configured. After running a job from Jenkins, a run is automatically created in Allura.



