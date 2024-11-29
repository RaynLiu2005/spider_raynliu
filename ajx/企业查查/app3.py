import json
import time
import requests
import csv
from lxml import etree
import re
def get_html(url,page):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
              "cookie":"JSESSIONID = 495EB112CDEBF0AC15078968BFE342A7",
              "Content - Type":"application / x - www - form - urlencoded;charset = UTF - 8"}
    try:
        data = {'page':page}
        r = requests.post(url,headers=header,data=data)
        r.raise_for_status()
        r.encoding = "UTF-8"
        return r.text
    except Exception as e:
        print(e)


def xpath(html):
    txt = json.loads(html)
    rows = txt.get('rows', [])
    list1 = []
    for i in rows:
        list = [i.get('corpName', ''), i.get('companyType'), i.get('oeriodCode'), i.get('creditCode'),
                i.get('evaGrade'), i.get('doScore')]
        url = f"https://www.qcc.com/web/search?key={list[0]}"

        detail_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.8121 SLBChan/111 SLBVPV/64-bit",
            "Cookie":
                "QCCSESSID=587ada5f4981bda628943820fa; qcc_did=bd8517ba-ee54-4fd3-8196-439d505e6117; UM_distinctid=192be676b411835-0f85fc52ec5193-26011951-172698-192be676b422702; acw_tc=0a47308417297762485598706e00828a6e43c653ad7741cdb244bd761b07fa; CNZZDATA1254842228=406809527-1729771302-%7C1729776265; tfstk=fMamHqY6NoojE1-oZgufj_hUvXIJGIgshRLtBVHN4YkWHKLY_VkgQYUxHS32QF2iFAhtklLiIWM51sMOhCD8pRcTkPUgVFVQ1rCjWsgbGVgNp9QKSSNj5wLBSPfKzQlgad8VHEzaCVgNpTn08k1S5JOicbUaa_ct6A84QxRzaYGiQFyZ30JrtXgZ7VyZzQlZtf8qbc8yaYGZ7jyZ7AtyLxHxpzWfdMIJcybQGjmmIFHyS4UWJmHFsY89WYlmmQVqEF8aru3sfuMVAQHskxNjiR_Blqogbr3zuT7Z8kwuSDuhXsgUl5rQb79csxP8hy04-tYxwcD04rok_FuryooUj-XDcxrYEDGr4CbIwJHzGrrl1LP4px0qa0QFt7oa2riQkT8m8kNxklyFenH4xfSPF3-EZ7Tsa1UyfhiqNbDpLJinTVCv95ClZHPS0bGbz_fkfhiqNbDdZ_xU8mlSGz5"
        }

        r = requests.get(url, headers=detail_headers)
        q_html = r.text
        doc = etree.HTML(q_html)

        # 使用正则表达式提取信息，并检查结果是否为空
        legal_representative = re.findall(re.compile(r'法定代表人：.*?<a .*?>(.*?)</a>', re.S), q_html)
        registered_capital = re.findall(re.compile(r'注册资本：.*?<span .*?>(.*?)</span>', re.S), q_html)
        address = re.findall(
            re.compile(r'地址：.*?<span .*?>.*?<span.*?>.*?<span.*?>.*?<span.*?>.*?<span.*?>(.*?)</span>', re.S), q_html)

        # 检查是否找到了匹配项，如果没有找到则使用空字符串代替
        legal_representative = legal_representative[0] if legal_representative else ''
        registered_capital = registered_capital[0] if registered_capital else ''
        address = address[0] if address else ''

        list2 = [list[0], list[1], list[2], list[3], list[4], list[5], legal_representative, registered_capital,
                 address]
        list1.append(list2)
        print(list1)
    return list1
def save(out_list,file):
    with open(file, "a+", encoding="UTF-8", newline="") as f:
        csv_write = csv.writer(f)
        csv_write.writerows(out_list)
if __name__ == "__main__":
    url = "https://hwdms.mot.gov.cn/BMWebSite/evaluate/getEvaluateList.do"
    for page in range(1,300):
        time.sleep(1)
        html = get_html(url,page)
        print(f"第{page}页爬取成功")
        result = xpath(html)
        save(result,"output.csv")
    print("保存成功")