import allure
from tochka_tests.model.pages.vacancies_page import VacanciesPage


def test_should_have_exact_title(setup_browser):
    browser = setup_browser

    with allure.step("browser open"):
        browser.open("/hr/vacancies")

    with allure.step('main title "Вакансии"'):
        VacanciesPage().should_have_exact_main_title('Вакансии')

    with allure.step('title "Выбери направление работы"'):
        VacanciesPage().should_have_exact_title('Выбери направление работы')

    with allure.step('title "Опыт работы"'):
        VacanciesPage().should_have_exact_title('Опыт работы')

    with allure.step('title "Как хочешь работать"'):
        VacanciesPage().should_have_exact_title('Как хочешь работать')


def test_choice_of_work(setup_browser):
    browser = setup_browser

    browser.open("/hr/vacancies")
    with allure.step('set IT work'):
        VacanciesPage().set_vacancy_parameters('IT')

    with allure.step('set work experience "1-3 лет"'):
        VacanciesPage().set_vacancy_parameters('От 1 года до 3 лет')

    with allure.step('set remote work'):
        VacanciesPage().set_vacancy_parameters('Удалённо')

    with allure.step('tester position selection'):
        VacanciesPage().choose_a_job('Тестировщик')

    with allure.step('opened a page with a vacancy "Тестировщик"'):
        VacanciesPage().should_have_exact_page('Тестировщик')


def test_vacancies_in_yekaterinburg(setup_browser):
    browser = setup_browser

    browser.open("/hr/vacancies")
    with allure.step('set city Yekaterinburg'):
        VacanciesPage().set_cities('Екатеринбург')

    with allure.step('vacancy is present in Yekaterinburg'):
        VacanciesPage().choose_a_job('Тестировщик')


