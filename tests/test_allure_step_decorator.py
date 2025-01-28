import allure
from selene import browser, be, have
from selene.api import s


@allure.step("Открываем главную страницу GitHub")
def open_github():
    browser.open('/')


@allure.step("Ищем репозиторий '{repo_name}'")
def search_repository(repo_name: str):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo_name).press_enter()


@allure.step("Переходим в репозиторий '{repo_name}'")
def open_repository(repo_name: str):
    s('.search-title').should(have.exact_text(repo_name)).click()


@allure.step("Открываем вкладку Issues")
def open_issues_tab():
    s('#issues-tab').click()


@allure.step("Проверяем наличие Issue с текстом '{issue_text}'")
def verify_issue_text(issue_text: str):
    s('.ListItem-module__listItem--kHali').should(have.text(issue_text))
    s('.ListItem-module__listItem--kHali').should(be.visible)


def test_clean_issue():
    open_github()
    search_repository("eroshenkoam/allure-example")
    open_repository("eroshenkoam/allure-example")
    open_issues_tab()
    verify_issue_text("Тестируем тест")
