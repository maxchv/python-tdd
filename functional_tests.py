from selenium import webdriver

browser = webdriver.Firefox(executable_path='e:\geckodriver.exe')
try:
    browser.get('http://localhost:8000')
    assert 'Django' in browser.title
except Exception as ex:
    print(ex)
finally:
    browser.quit()