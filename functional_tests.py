from selenium import webdriver

browser = webdriver.Firefox(executable_path='e:\geckodriver.exe')

# Edith has heard about a copy new online to-do app.
# She goes to check out its homepage
browser.get('http://localhost:8000')

# She notice the page title a heard mention to-do list
assert 'Django' in browser.title

# Sh is invited to enter a to-do item straight away

# She types 'Buy peacock feathers" into a text box
# (Edith's hobby is tying fly-finishing lures)

# TODO: complete tasks
