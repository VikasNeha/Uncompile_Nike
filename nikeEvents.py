# Embedded file name: PageEvents\nikeEvents.pyo
from webpageEvents import WebpageEvents
from Utilities.constants import IDMODE
import sys
import time

class NikeEvents(WebpageEvents):

    def __init__(self):
        super(NikeEvents, self).__init__()

    def destroy(self):
        super(NikeEvents, self).destroy()

    def loginToNike(self, Nike_Username, Nike_Password):
        self.enterText(IDMODE.ID, 'exp-login-email', Nike_Username)
        self.enterText(IDMODE.ID, 'exp-login-password', Nike_Password)
        self.clickElement(IDMODE.ID, 'exp-login-rememberMe')
        self.findElement(IDMODE.ID, 'exp-login-password').submit()

    def select_size_and_add_to_cart(self, size):
        sizeBox = self.findElement(IDMODE.CLASS, 'exp-pdp-size-and-quantity-container')
        select2 = sizeBox.find_element_by_tag_name('a')
        select2.click()
        time.sleep(1)
        lis = sizeBox.find_elements_by_tag_name('li')
        for li in lis:
            if li.text.strip() == size:
                li.click()
                break

        time.sleep(1)
        button = self.findElement(IDMODE.CLASS, 'exp-pdp-save-container')
        button.find_element_by_tag_name('button').click()