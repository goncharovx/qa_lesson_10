import allure
from selene import browser, be, have
from selene.api import s


def test_clean_issue():
    with allure.step("Открываем главную страницу GitHub"):
        browser.open('/')

    with allure.step("Ищем репозиторий 'eroshenkoam/allure-example'"):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step("Переходим в репозиторий"):
        s('.search-title').should(have.exact_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем вкладку Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с текстом 'Тестируем тест'"):
        s('.ListItem-module__listItem--kHali').should(have.text('Тестируем тест'))
        s('.ListItem-module__listItem--kHali').should(be.visible)
