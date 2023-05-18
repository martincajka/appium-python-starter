import os
import unittest
# iOS environment
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
# Example of test run using cloud service SauceLabs https://saucelabs.com/

caps = {}
caps['platformName'] = 'iOS'
caps['appium:app'] = 'storage:filename=UICatalog.app.zip'  # The filename of the mobile app
caps['appium:deviceName'] = 'iPhone Simulator'
caps['appium:deviceOrientation'] = 'portrait'
caps['appium:platformVersion'] = '16.1'
caps['appium:automationName'] = 'XCUITest'
caps['sauce:options'] = {}
caps['sauce:options']['build'] = 'appium-build-RK8VC'  # appium build can be anything, helps you to find test results
caps['sauce:options']['name'] = 'UICatalog demo test'

# url is obtained from system variable as it contains some confidential information.
# This URL is generated by saucelabs during process of setting up run
# For how to store environment variables on MacBook check following link:
# https://blog.adamgamboa.dev/how-to-set-environment-variable-in-macos/
appium_server_url = os.environ.get('SAUCELABS_URL')


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, caps)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_open_action_sheets(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Action Sheets')
        el.click()


if __name__ == '__main__':
    unittest.main()
