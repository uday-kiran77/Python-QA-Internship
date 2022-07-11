# Android app test script version 1
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.mobileby import MobileBy


# Capabilities option for selecting application
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "7.0",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.test.contactformv2",
    "appium:app": "C:\\Users\\uday\\Desktop\\Internship Project\\appium\\app_v2\\formv2.apk",

}

# initialise web driver using appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
driver.back()


# Select Text fields using xpath and send values to input form
driver.find_element(
    By.ID, "com.test.contactformv2:id/nameTV").send_keys("Uday")
driver.find_element(
    By.ID, "com.test.contactformv2:id/emailTV").send_keys("udaykiran@gmail.com")
# Toggle switch
driver.find_element(By.ID, "com.test.contactformv2:id/featureSW").click()
# select country
driver.find_element(By.ID, "com.test.contactformv2:id/countrySpinner").click()
driver.find_element(
    By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]").click()


# Scroll down
driver.swipe(100, 700, 100, 150)

driver.find_element(By.ID, "com.test.contactformv2:id/radioMale").click()
driver.find_element(
    By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox").click()


# Click submit button, located using its ID
driver.find_element(By.ID, "com.test.contactformv2:id/submitButton").click()

# Check for error in form
try:
    assert 'Please Fillout all fields' not in driver.find_element(
        By.ID, "com.test.contactformv2:id/uError").text
except AssertionError:
    print("Test Failed ")
else:
    print("Test Passed")

# Click Clear button, located using its ID
driver.find_element(By.ID, "com.test.contactformv2:id/clearButton").click()
time.sleep(2)

# Close App
driver.close_app()
