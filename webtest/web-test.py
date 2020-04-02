# -*- encoding=utf8 -*-
from selenium import webdriver
import time
import os
# 生成年月日时分秒时间
picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print(picture_time)
print(directory_time)
# 打印文件目录
print(os.getcwd())
# 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
try:
    File_Path = os.getcwd() + '\\' + directory_time + '\\'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
        print("目录新建成功：%s" % File_Path)
    else:
        print("目录已存在！！！")
except BaseException as msg:
    print("新建目录失败：%s" % msg)
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(20)
driver.get("http://activity.fm.easttone.com/system/login.do")
time.sleep(2)
# 输入用户名（记者）
driver.find_element_by_xpath("//*[@id='username']").send_keys("shopqp")
# 输入密码
driver.find_element_by_xpath("//*[@id='password']").send_keys("shop@qingpu")
time.sleep(5)
# 点击登陆按钮
driver.find_element_by_xpath("//*[@id='loginform']/input[5]").click()
try:
    url=driver.save_screenshot('/Users/wenjiehe/Documents/GitHub/testapi-hewenjie/webtest/picture' + picture_time + '.png')
    print("%s ：截图成功！！！" % url)
except BaseException as pic_msg:
    print("截图失败：%s" % pic_msg)
# 退出
driver.quit()