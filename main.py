from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "hovdikruslan@gmail.com"
password = "HondaRoyal0401!"
actions.login(driver, email, password)
# person = Person(company="Boostify", driver=driver)
person = Person(linkedin_url=None, name=None, about=[], experiences=[], educations=[], interests=[], accomplishments=[], company="Boostify", job_title=None, driver=None, scrape=True)
print(person)