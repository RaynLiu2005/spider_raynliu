# jason爬虫例子
import json
import time
import requests

url = ("http://61.190.26.79:5000/General/alljudge_json?page={}&limit=20&jtype=0&chnm=&apti=&result=&st=0")

headers = {

    # "Cookie": "JSESSIONID=C65B0E122107C99F2B6B0EE6397CD80A",
    "Referer": "http://61.190.26.79:5000/Home/lstJUDGE",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

}


for number in range(1, 3):
    time.sleep(3)

    res = requests.get(url.format(number), headers=headers)
    # print(res.text)
    # , "data": [{"ID": 1481507, "UNITNAME": "安徽省水利水电 (部分输出)
    data = json.loads(res.text)
    items = data['data']
    # print(items)

# 遍历数组独享
    for item in items:
        id = item.get('ID')
        unit_name = item.get('UNITNAME')
        address = item.get('ADDRESS').replace("\r", "").replace("\n", "").replace("\t", "").replace(" ", "")
        apti = item.get('APTI').replace("\r", "").replace("\n", "").replace("\t", "").replace(" ", "")
        score = item.get('SCORE')
        line = (str() + "-" + str(unit_name) + "-" + str(address) + "-" + str(apti) + "-" + str(score))
    #
        print(line)
    #
        with open('./安徽省水利建设市场信用信息.txt', 'a+', encoding='utf-8') as f:
            f.write(line + "\n")
