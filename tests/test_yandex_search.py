from pages.search_page import SearchPage


def test_yandex_search(browser):
    main_page = SearchPage(browser, "https://yandex.ru/")
    main_page.open()
    main_page.search("гугл")
    assert main_page.should_be_drop_down_list()
    main_page.submit_search_by_enter()
    assert main_page.link_in_first_five_result()

