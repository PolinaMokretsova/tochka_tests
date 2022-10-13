from selene import have
from selene.support.shared import browser


class HRPage:

    def should_have_exact_hr_title(self, param):
        browser.element('div.hr_heroTitle__GYYT2.h1').should(have.text(param))

    def should_have_exact_body(self, param):
        browser.element('p.hr_heroText__4Lz0_.fs-l').should(have.text(param))

    def click_button(self,param):
        browser.element('button.tab_tabButton___PexF').should(have.text(param)).click()

    def click_link_all_vacancies(self):
        browser.element('a.link-next_commonLinkNext__4wIWR.mt-2.mb-xs-5').click()