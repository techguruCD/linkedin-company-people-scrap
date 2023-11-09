from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "hovdikruslan@gmail.com"
password = "HondaRoyal0401!"
actions.login(driver, email, password)
person = Person("https://www.linkedin.com/in/joey-sham-aa2a50122", driver=driver)
print(person)