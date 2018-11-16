import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.cyanogenmod.filemanager'
desired_caps['appActivity'] = '.activities.NavigationActivity'
desired_caps['automationName'] = 'Uiautomator2'
# desired_caps['noReset'] = True


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2)

driver.press_keycode(4)
time.sleep(1)
driver.press_keycode(4)
time.sleep(1)
driver.press_keycode(4)


# print(WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'再次点击')]")).text)


print(driver.find_element_by_xpath("//*[@text='再次点击即可退出.']").text)



time.sleep(5)

