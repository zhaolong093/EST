from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")


hover = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//ul[@class='navbar-nav horizontal']/li[6]")))
ActionChains(driver).move_to_element(hover).perform()

rbtn = driver.find_element(By.XPATH, "//ul[contains(@class,'mz-sub-menu-96') and contains(@class,'dropdown-menu')]/li[2]/a")
driver.execute_script("arguments[0].click();", rbtn)

fname = driver.find_element(By.NAME, "firstname").send_keys("abcd")
lname = driver.find_element(By.NAME,"lastname").send_keys("dcba")
email = driver.find_element(By.NAME, "email").send_keys("abcd.dcba@example.com")
phone = driver.find_element(By.NAME, "telephone").send_keys("041234567")
pwd = driver.find_element(By.NAME, "password").send_keys("abcd$dcba")
cpwd = driver.find_element(By.NAME, "confirm").send_keys("abcd$dcba")
chk = driver.find_element(By.NAME, "agree")
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", chk)
driver.execute_script("arguments[0].click();", chk)

submit = driver.find_element(By.CSS_SELECTOR, "input.btn-primary[value='Continue']" )
submit.submit()

time.sleep(10)


driver.quit()



#firstname, lastname, email, telephone, password, confirm,


