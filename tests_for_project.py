from selene import be, have, browser
import time


def test_search(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_bad_search(open_google):
    input_text = 'asghtyjcnbkuyepoekheie'
    browser.element('[type="search"]').type(input_text).press_enter()
    browser.element('[class="card-section"]').should(have.text('ничего не найдено'))
    time.sleep(5)