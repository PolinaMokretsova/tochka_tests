from selene import have
from selene.support.shared import browser

from tochka_tests.model.controls.dropdown import Dropdown


class VacanciesPage:

    def should_have_exact_main_title(self, param):
        browser.all('div.h2.mb-9.mb-xs-2').element_by(have.text(param))

    def should_have_exact_title(self, param):
        browser.all('div.jobs_jobsFilterLabel__WGUvD.mb-2').element_by(have.text(param))

    def set_vacancy_parameters(self, param):
        browser.all('button.tab_tabButton___PexF').element_by(have.text(param)).click()

    def choose_a_job(self, param):
        browser.all('div.jobs_jobsListItemName__jJA4E').element_by(have.text(param)).click()

    def should_have_exact_page(self, param):
        browser.element('h1.mb-6.mb-m-4.mb-xs-3').should(have.text(param))

    def set_cities(self,param):
        city = Dropdown(browser.element('div.input-dropdown_icon__6mn63'))
        city.select(option=param)
