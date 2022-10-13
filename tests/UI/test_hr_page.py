import allure
from tochka_tests.model.pages.hr_page import HRPage
from tochka_tests.model.pages.vacancies_page import VacanciesPage


def test_should_have_exact_title_hr(setup_browser):
    browser = setup_browser

    with allure.step("browser open"):
        browser.open("/hr")

    with allure.step('title "давай работать"'):
        HRPage().should_have_exact_hr_title('Давай работать')


def test_correct_body(setup_browser):
    browser = setup_browser

    browser.open("/hr")
    with allure.step(
            'body "Без корпоративной иерархии и бюрократии, дресс-кода и компромиссов с собой, потолка в развитии и зарплате."'):
        HRPage().should_have_exact_body(
            'Без корпоративной иерархии и бюрократии, дресс-кода и компромиссов с собой, потолка в развитии и зарплате.')


def test_click_it_button(setup_browser):
    browser = setup_browser

    browser.open("/hr")
    with allure.step('click "it" button'):
        HRPage().click_button('IT')

    with allure.step('opened it vacancies'):
        VacanciesPage().should_have_exact_main_title('Вакансии')


def test_see_all_vacancies(setup_browser):
    browser = setup_browser

    browser.open("/hr")
    with allure.step('click "смотреть все вакансии"'):
        HRPage().click_link_all_vacancies()

    with allure.step('opened vacancies page'):
        VacanciesPage().should_have_exact_main_title('Вакансии')

