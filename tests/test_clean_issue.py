from selene import browser, be, have
from selene.api import s


def test_clean_issue():
    # Открываем браузер
    browser.open('/')

    # Заполняем поле поиска
    s('.header-search-button').click()
    s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    # Переходим в репозиторий
    s('.search-title').should(have.exact_text('eroshenkoam/allure-example')).click()

    # Переходим к табу Issue
    s('#issues-tab').click()

    # Проверяем наличие Issue c номером 95
    s('.ListItem-module__listItem--kHali').should(have.text('Тестируем тест'))
    s('.ListItem-module__listItem--kHali').should(be.visible)
