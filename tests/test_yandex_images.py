from pages.search_page import SearchPage


def test_yandex_imgs(browser):
    # Open main_page
    main_page = SearchPage(browser, "https://yandex.ru/")
    main_page.open()
    # Go to images page
    images_page = main_page.go_to_images_page()
    assert images_page.is_it_images_pages()
    # Click_by_first_picture and go to view
    images_page.choose_pic()
    #  get image as base64
    first_image = images_page.get_pic_as_base64()
    # go to next image
    images_page.go_to_next_pic()
    # get image as base64
    second_image = images_page.get_pic_as_base64()
    # comparing images, images should be different
    assert first_image != second_image, "There are two identical images"
    # back to first picture
    images_page.back_to_previous_pic()
    # get image as base64
    first_image_again = images_page.get_pic_as_base64()
    # comparing images, images should be equal
    assert first_image == first_image_again, "Images are not identical"
