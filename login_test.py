# login_test.py
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome browser (you need ChromeDriver installed)
driver = webdriver.Chrome()

# Open sample website
driver.get("https://example.com/login")

# Find username and password fields
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

# Enter sample data
username.send_keys("testuser")
password.send_keys("testpass")

# Click login button
login_button = driver.find_element(By.NAME, "login")
login_button.click()

print("Login automation test completed")
driver.quit()
