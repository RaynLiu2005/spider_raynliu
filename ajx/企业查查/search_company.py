# -*- coding: utf-8 -*-
import time
import csv
import pandas as pd
from selenium import webdriver

df = pd.read_csv("tantong4.csv", sep=",", encoding="utf-8")


def save_csv(item, path):
    with open(path, "a+", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(item)


def upload_file():
    # 创建一个WebDriver实例
    wd = webdriver.Chrome("chromedriver.exe")

    # 打开网页
    wd.get('https://www.sscha.com/?activityCode=ACTIVITY1734809570418905090&channelCode=%27%27CHANNE'
           'L1734771540567814145&channelShareCode=74567717&type=PC&mAcc=suzhou002&bd_vid=11336369941781896800')
    data = []
    time.sleep(15)
    count = 1
    # 使用for循环进行多次操作
    for i in df['公司名称']:
        # 在输入框中输入文字
        if count <= 1:
            wd.find_element_by_xpath('//*[@id="searchInputHomeRef"]').send_keys(i)
            time.sleep(5)
            wd.find_element_by_xpath('//*[@id="searchInputId"]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]'
                                     '/div/span[2]').click()
            time.sleep(5)
        if count >= 2:
            input_box = wd.find_element_by_xpath('//*[@id="searchInputCompRef"]')
            input_box.click()
            # 清空输入框内容
            input_box.clear()
            time.sleep(5)
            input_box.send_keys(i)
            time.sleep(7)
            wd.find_element_by_xpath(
                '//*[@id="searchPublicInputId"]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]').click()
            time.sleep(5)
        wd.switch_to.window(wd.window_handles[-1])
        time.sleep(6)
        try:
            suspondWindow = wd.find_element_by_xpath(
                "//*[@id='__layout']/div/div[2]/div/div/div[14]/div/div[2]/div[1]/i")
            suspondWindow.click()
        except Exception as e:
            pass

        # 等待页面元素出现或变化
        # 定义滑动距离和滑动间隔时间（单位：像素和秒）
        scroll_distance = 50  # 每次滑动的距离
        scroll_interval = 0.1  # 滑动间隔时间
        # 缓慢向下滑动页面
        for m in range(15):  # 滑动10次，可以根据需要调整次数
            wd.execute_script("window.scrollBy(0, %d);" % scroll_distance)
            time.sleep(scroll_interval)
        # 刷新页面
        time.sleep(7)
        for row in wd.find_elements_by_xpath('//*[@id="changeRecordData"]/div[3]/div/div[2]/div[1]/div/table'):
            credit = row.find_element_by_xpath('tbody/tr[1]/td[4]/div/span/div/div/div').text
            person = row.find_element_by_xpath('tbody/tr[2]/td[2]/div/span/div/span/div/div[2]/a/span').text
            fund = row.find_element_by_xpath('tbody/tr[3]/td[2]/div/span').text
            e_type = row.find_element_by_xpath('tbody/tr[5]/td[2]/div/span').text
            e_enter = row.find_element_by_xpath('tbody/tr[8]/td[2]/div/span').text
            address = row.find_element_by_xpath('tbody/tr[9]/td[2]/div/span/div/div/div').text
            validity = row.find_element_by_xpath('tbody/tr[5]/td[4]/div/span').text
            taxation = row.find_element_by_xpath('tbody/tr[7]/td[6]/div/span').text
            data.append([credit, person, fund, e_type, e_enter, address, validity, taxation])
        count += 1
        print(data)
        save_csv(data, 'found_1tt.csv')
        data = []
        # 点击搜索按钮
    # 关闭浏览器
    wd.quit()


if __name__ == "__main__":
    upload_file()  # 登录网站及新建文件夹