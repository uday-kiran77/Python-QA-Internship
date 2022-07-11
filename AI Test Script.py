import time
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class test_ai_classifier(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = 'UiAutomator2'

        # for app 01
        desired_caps['appPackage'] = 'com.test.classifiertest01'
        desired_caps['appActivity'] = 'com.test.classifiertest01.MainActivity'

        # for app 02
        # desired_caps['appPackage'] = 'com.test.classifiertest02'
        # desired_caps['appActivity'] = 'com.test.classifiertest02.MainActivity'

        desired_caps['skipServerInstallation'] = True
        desired_caps['customFindModules'] = {'ai': 'test-ai-classifier'}
        desired_caps['shouldUseCompactResponses'] = False
        desired_caps['skipServerInstallation'] = True

        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_ai(self):
        driver = self.driver

        driver.find_element(MobileBy.CUSTOM, 'ai:user').click()
        time.sleep(1)
        driver.back()

        driver.find_element(MobileBy.CUSTOM, 'ai:mail').click()
        time.sleep(1)
        driver.back()

        driver.find_element(MobileBy.CUSTOM, 'ai:settings').click()
        time.sleep(1)
        driver.back()

        driver.find_element(MobileBy.CUSTOM, 'ai:camera').click()
        time.sleep(1)
        driver.back()

        driver.find_element(MobileBy.CUSTOM, 'ai:bookmark').click()
        time.sleep(1)
        driver.back()

        driver.find_element(MobileBy.CUSTOM, 'ai:alarm').click()
        time.sleep(1)
        driver.back()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_ai_classifier)
    unittest.TextTestRunner(verbosity=2).run(suite)
