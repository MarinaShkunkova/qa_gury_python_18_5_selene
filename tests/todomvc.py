from selene import browser, have, be


def test_complete_todo():
    browser.open('/')
    browser.element('.new-todo').type('a').press_enter()



    browser.all('.todo-list>li').should(have.size(1))
