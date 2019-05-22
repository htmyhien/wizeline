import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 

def find_element_by_xpath(driver, xpath):
    result = None
    try:
        result = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return result
    return result

def find_element_by_name(driver, name):
    result = None
    try:
        result = driver.find_element_by_name(name)
    except NoSuchElementException:
        return result
    return result

def find_element_by_id(driver, id):
    result = None
    try:
        result = driver.find_element_by_id(id)
    except NoSuchElementException:
        return result
    return result

DRIVER_BIN = 'C:/wizeline/bin/chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_BIN)

driver.get ('https://www.saucedemo.com')
time.sleep(3) # Let the user actually see something!

#LOGIN test case
user_name_we = find_element_by_id(driver, 'user-name')
assert(user_name_we is not None)
user_name_we.send_keys('standard_user')

password_we = find_element_by_id(driver, 'password')
assert(password_we is not None)
password_we.send_keys('secret_sauce')


login_button = find_element_by_xpath(driver, '//*[@id="login_button_container"]/div/form/input[3]')
assert(login_button is not None)
login_button.click()

time.sleep(3) # Let the user actually see something!

products_text_we = find_element_by_xpath(driver, '//div[contains(text(), "' + 'Products' + '")]')
assert(products_text_we is not None)

# Order or Add To Cart test case

add_to_cart_button = find_element_by_xpath(driver, '//button[contains(text(), "' + 'ADD TO CART' + '")]')
assert(add_to_cart_button is not None)
add_to_cart_button.click()

time.sleep(3) # Let the user actually see something!

remove_button = find_element_by_xpath(driver, '//button[contains(text(), "' + 'REMOVE' + '")]')
assert(remove_button is not None)

time.sleep(3) # Let the user actually see something!

# ...

driver.quit()

