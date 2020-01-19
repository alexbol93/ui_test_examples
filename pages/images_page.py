from pages.base_page import BasePage


class ImagesPage(BasePage):

    def choose_pic(self):
        self.browser.find_element_by_css_selector('[class="cl-teaser__wrap cl-teaser-video-play"]').click()

    def go_to_next_pic(self):
        self.browser.find_element_by_css_selector('[title="Следующая"]').click()

    def back_to_previous_pic(self):
        self.browser.find_element_by_css_selector('[title="Предыдущая"]').click()

    def get_pic_as_base64(self):
        return self.browser.find_element_by_css_selector('[class="image__image"]').screenshot_as_base64

    def compare_two_pic(self, pic1, pic2):
        if pic1 == pic2:
            return True
        else:
            return False

    def is_it_images_pages(self):
        current_url = self.browser.current_url
        if current_url == "https://yandex.ru/images/":
            return True
        else:
            return False
