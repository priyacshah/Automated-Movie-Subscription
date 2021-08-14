from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

# Github credentials
username = "priya"
password = "12345"

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver")

# head to github login page
driver.get("http://3.96.76.163/")

link = driver.find_element_by_link_text('Login')
link.click()

# find username/email field and send the username itself to the input field
driver.find_element_by_name("username").send_keys(username)

# find password input field and insert password as well
driver.find_element_by_name("password").send_keys(password)

# click login button
driver.find_element_by_name("submit").click()


driver.find_element_by_id("submit1").click()

