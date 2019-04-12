
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
execute_path = os.path.join(BASE_DIR,'chromedriver.exe')
class TrySelenium():
    """测试读取百度文库"""

    def getChrome(self):
        """获取浏览器对象,和等待时间"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        #无头模拟
        browser = webdriver.Chrome(executable_path=execute_path,chrome_options=chrome_options)
        # browser = webdriver.Chrome(executable_path=execute_path)
        #延时等待
        wait = WebDriverWait(browser,10)

        return browser,wait


    def do_try(self,url):
        """尝试打开"""
        browser,wait = self.getChrome()
        browser.switch_to.window(browser.window_handles[0])
        browser.get(url=url)
        #延时2秒
        time.sleep(2)
        print("打印采集的信息")
        #找到百度文库it/计算机目录类
        button = wait.until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="wk-all-cate"]/dl[2]/dd/a[2]'))
        )
        if button.text == 'IT/计算机':
            time.sleep(2)
            print('点击跳转',button.text)
            print('打印采集到的a标签的链接属性',button.get_attribute('href'))
            button.click()
            time.sleep(20)
        # text = browser.page_source
        # print('打印页面内容',text)

if __name__ =="__main__":
    tryselenium = TrySelenium()
    url = 'https://wenku.baidu.com/'
    print("开始请求数据")
    tryselenium.do_try(url=url)
    print("打印数据完毕")
