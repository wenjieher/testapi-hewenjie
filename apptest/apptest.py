from appium import webdriver
import time
from apptest.appkeys import *
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '7.1.1', # 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.wdit.shrmtxh.test', # 启动APP Package名称
  'appActivity': 'com.wdit.shrmt.android.ui.main.RmShSplashActivity', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(20)

gbBtn = driver.find_elements_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/btn_cancel']")
if (gbBtn):
  driver.keyevent(4)
else:
  print('good')

#driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/btn_cancel']").click()

swipeUp(driver,6000,1)

eles = driver.find_elements_by_id("tv_title")

for ele in eles:
    # 打印标题
    print(ele.text)

# 根据id定位搜索位置框，点击
driver.find_element_by_xpath("//*[@text='人文']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='不断提高人民群众获得感']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/btn_click_sc']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/btn_click_sc']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/et_click_input_comment']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/et_comment']").send_keys('good')
time.sleep(1)
driver.find_element_by_xpath("//*[@resource-id='com.wdit.shrmtxh.test:id/tv_click_fa_bu']").click()
time.sleep(1)
driver.quit()
