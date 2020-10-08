from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

# команда для неявного ожидания со значением по умолчанию в 10:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

# реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента:
# как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
# Чтобы перехватывать исключение, нужна конструкция try/except:

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

