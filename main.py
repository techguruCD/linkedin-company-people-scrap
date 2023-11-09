from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "hovdikruslan@gmail.com"
password = "HondaRoyal0401!"
actions.login(driver, email, password)
person = Person(company="Boostify", driver=driver)
print(person)