from typing import Optional
from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            'div.col-xl-8 col-m-12 col-xs-6'
        ).element_by(have.text(autocomplete or from_)).click()

    def autocomplete(self, option: str):
        self.element.type(option).press_enter()

