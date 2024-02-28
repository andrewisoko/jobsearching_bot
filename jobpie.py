

from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random 



random_time = random.randrange(2,11)


 
# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 

# Disabling password manager pop up
prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False}
options.add_experimental_option("prefs", prefs)


 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
options.add_experimental_option("detach",True)
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 



 
driver.get("https://www.reed.co.uk/")



accept_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/button")
time.sleep(random_time)
accept_button.click()



what = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[4]/div/section[1]/main/form/div/div/div/div[1]/span/input")
time.sleep(random_time)
what.send_keys("Entry level") 


where = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div/section[1]/main/form/div/div/div/div[2]/span/input")
time.sleep(random_time)
where.send_keys("Manchester City Centre") 


search_jobs = driver.find_element(By.ID , "homepageSearchButton")
time.sleep(random_time)
search_jobs.click()


sign_in = driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div[2]/div/ul/li[2]/a")
time.sleep(random_time)
sign_in.click()



email_bar = driver.find_element(By.ID,"signin_email")
time.sleep(random_time)
email_bar.send_keys("Andrewmain2020@outlook.com" + Keys.ENTER)


password_bar = driver.find_element(By.ID , "signin_password")
time.sleep(random_time)
password_bar.send_keys("Dorosoko1001*") 


continue_button = driver.find_element(By.ID , "signin_button")
time.sleep(random_time)
continue_button.click()


wait = WebDriverWait(driver, 10)
last_week = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/aside/div[2]/div/div[7]/div[2]/div/select/option[4]")))
time.sleep(random_time)
last_week.click()

# wait_again = WebDriverWait(driver,20)

easy_apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Easy apply')]")

time.sleep(random_time)
driver.execute_script("arguments[0].click();", easy_apply_button)

submit_application = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.apply-job-modal_buttonGroup__button__6ObMn.btn.btn-primary')))
time.sleep(random_time)
submit_application.click()



ok_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.application-confirmation-modal_continueButton__i73Dl.btn.btn-primary')))
time.sleep(random_time)
ok_button.click()

print("application completed") 


