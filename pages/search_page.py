from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.images_page import ImagesPage


class SearchPage(BasePage):

    def search(self, text):
        input_box = self.browser.find_element_by_xpath("//input[@class='input__control input__input']")
        input_box.clear()
        input_box.send_keys(text)

    def should_be_drop_down_list(self):
        try:
            popup = self.browser.find_element_by_css_selector('div[class="suggest2__content suggest2__content_theme_normal"]')
            return True
        except NoSuchElementException:
            return False

    def submit_search_by_enter(self):
        input_box = self.browser.find_element_by_xpath("//input[@class='input__control input__input']")
        input_box.send_keys(Keys.RETURN)

    def link_in_first_five_result(self):
        first_five_result = self.browser.find_elements_by_css_selector('li[data-cid] h2 a')[0:5]
        for i in first_five_result:
            link = i.get_attribute("href")
            if link == "https://www.google.ru/":
                return True
        return False

    def go_to_images_page(self):
        images_link = self.browser.find_element_by_css_selector('[data-id="images"]')
        images_link.click()
        return ImagesPage(self.browser, self.url)