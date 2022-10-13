from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element: Element):
        self.element = element

    def select(self, /, *, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('div.input-dropdown_item__UQ9A8').element_by(have.exact_text(option)).click()

    def autocomplete(self, /, *, option: str):
        self.element.all(
            'div.input-dropdown_item__UQ9A8'
        ).element_by(have.exact_text(option)).click()

