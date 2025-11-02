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

rbtn = driver.find_element(By.XPATH, "//ul[contains(@class,'mz-sub-menu-96') and contains(@class,'dropdown-menu')]/li[1]/a")
driver.execute_script("arguments[0].click();", rbtn)

driver.find_element(By.NAME, "email").send_keys("abcd.dcba@example.com")
driver.find_element(By.NAME, "password").send_keys("abcd$dcba")
btn = driver.find_element(By.CSS_SELECTOR, "input.btn-primary[value='Login']")
btn.click()


# email, password, submit

time.sleep(5)
driver.quit()