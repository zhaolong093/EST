from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=common/home")
lct = driver.find_element(By.CLASS_NAME,"shop-by-category")
lct.click()
print("lct1 work")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//ul[@class='navbar-nav vertical']/li")))

lct2 = driver.find_element(By.XPATH, "//ul[@class='navbar-nav vertical']/li[2]")
lct2.click()
print("lct2 work")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-compare")))
cbtns = driver.find_elements(By.CLASS_NAME, "btn-compare")
print("Found cbtn")
if len(cbtns) >= 2:
    for i in range(2):
        btn = cbtns[i]
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn )
        # reference to stackoverflow: https://stackoverflow.com/questions/56683305/how-to-click-on-the-image-selenium-python
        time.sleep(2)
        driver.execute_script("arguments[0].click();", btn)
        print(f"btn click {i+1}")
        time.sleep(2)
else:
    print("sth error")

driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=product/compare")
time.sleep(10)
print("100% work")
driver.quit()