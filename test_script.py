# Android app test script version 1
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.mobileby import MobileBy

# from testai_classifier import ClassifierClient


# Capabilities option for selecting application
desired_caps = {
    "platformName": "Android",
    "appium:platformVersion": "7.0",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.example.contactform",
    "appium:app": "C:\\Users\\uday\\Desktop\\Internship Project\\appium\\app_v1\\form.apk",

}

# initialise web driver using appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.implicitly_wait(10)
driver.back()


# Select Text fields using xpath and send values to input form
driver.find_element(
    by=By.ID, value="com.example.contactform:id/nameTV").send_keys("Uday")
driver.find_element(
    by=By.ID, value="com.example.contactform:id/emailTV").send_keys("udaykiran@gmail.com")
driver.find_element(
    by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]").send_keys("13/05/2002")
driver.find_element(
    by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[4]").send_keys("123456")

# Scroll down
driver.swipe(100, 700, 100, 150)

driver.find_element(
    by=By.ID, value="com.example.contactform:id/radioMale").click()
driver.find_element(
    by=By.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox").click()


# Click submit button, located using its ID
driver.find_element(
    by=By.ID, value="com.example.contactform:id/submitButton").click()

# Check for error in form
try:
    assert 'Please Fillout all fields' not in driver.find_element(
        By.ID, "com.example.contactform:id/errorContainer").text
except AssertionError:
    print("Test Failed ")
else:
    print("Test Passed")

# Click Clear button, located using its ID
driver.find_element(
    by=By.ID, value="com.example.contactform:id/clearButton").click()
time.sleep(2)

# Close App
driver.close_app()
