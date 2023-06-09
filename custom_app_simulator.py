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

options = XCUITestOptions()
options.platform_name = 'iOS'
options.automation_name = 'XCUITest'

# Platform version and device name is matching simulator that is available at my MacBook, to use relevant simulator
# on your machine check available devices using command:
# xcrun simctl list
options.platformVersion = '14.5'
options.device_name = 'iPhone 12'

# path to application package to be installed on simulator
options.app = os.path.abspath('UICatalog.app.zip')

# following options are doing some 'magic' that helps establish connection to real device
# based on hints from:
# https://stackoverflow.com/questions/69315482/appium-and-desktop-unable-to-launch-wda-session-since-xcode13-and-ios15
# https://discuss.appium.io/t/unable-to-start-webdriveragent-session-because-of-xcodebuild-failure/24542/9
options.new_command_timeout = '60'
options.wda_startup_retries = '3'
options.wda_startup_retry_interval = '20000'
options.wda_local_port = '8132'

appium_server_url = 'http://localhost:4723'
appium_service = AppiumService()


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        appium_service.start()
        # Appium1 points to http://127.0.0.1:4723/wd/hub by default
        self.driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
        if appium_service.is_running:
            appium_service.stop()

    def test_open_action_sheets(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Action Sheets')
        el.click()


if __name__ == '__main__':
    unittest.main()
