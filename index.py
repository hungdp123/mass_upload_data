
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os

chromedriver_location = r"C:\Users\hungd\Downloads\chromedriver_win32\chromedriver"
wovodat_login_button = '//*[@id="pagewrapper"]/div[3]/div/h3/a'
wovodat_username = '//*[@id="pagewrapper"]/div[3]/div/div[1]/table/tbody/tr[3]/td/input'
wovodat_password = '//*[@id="regisLoginpw"]/input'
wovodat_login = '//*[@id="submit"]'
upload_button = '//*[@id="pagewrapper"]/div[3]/div/div[1]/div[3]/ul[2]/li/p/a'
choose_file = '/html/body/div/div[3]/div/div[2]/div[2]/div/form/div[4]/input[1]'
ok_button = '/html/body/div/div[3]/div/div[2]/div[2]/div/form/div[4]/input[2]'
confirm_button = '//*[@id="pagewrapper"]/div[3]/div/div[1]/form[2]/input'


userName = //Enter username
password = //Enter password

filepath = "C:/Users/hungd/Downloads/EOS project/United States + Pacific Ocean (revised)/"
dirs = os.listdir(filepath)
for file in dirs:
    if file.endswith(".xml"):
        print("uploading " + file + " to database")
        file_name = filepath + file
        driver = webdriver.Chrome(chromedriver_location)
        driver.get('https://wovodat.org/populate/home_populate.php')
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, wovodat_login_button))).click()
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, wovodat_username))).send_keys(userName)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, wovodat_password))).send_keys(password)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, wovodat_login))).click()
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, upload_button))).click()
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, choose_file))).send_keys(file_name)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, ok_button))).click()
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, confirm_button))).click()
        //Remove the below comment if you want to remove the file from computer after uploading
        //os.remove(file_name) 
        print("Upload successful!")
        driver.quit()




