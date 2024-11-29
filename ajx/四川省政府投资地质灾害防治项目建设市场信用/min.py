# jason爬虫例子
import json
import time
import requests

url = ("http://zxpt.scdzfz.cn:17085/api/unitCreditList?page={}&limit=20&unitName=&unitType=")

headers = {

    # "Cookie": "JSESSIONID=C65B0E122107C99F2B6B0EE6397CD80A",
    "Referer": "http://zxpt.scdzfz.cn:17085/credit/index?page=xinyongpingjia",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"

}

for number in range(1, 22):
    time.sleep(1)

    res = requests.get(url.format(number), headers=headers)
    #    print(res.text)
    # , "data": [{"ID": 1481507, "UNITNAME": "安徽省水利水电 (部分输出)
    data = json.loads(res.text)
    items = data['data']
    print(items)
    # 遍历数组独享
    for item in items:
        unit_name= item.get('unitName'),
        creditRating= item.get('creditRating'),
        creditScore=item.get('creditScore'),
        ratingTime= item.get('ratingTime')
        line = (str(unit_name) + "-" + str(creditRating) + "-" + str(creditScore) + "-" + str(ratingTime))
        #
        print(line)

        #
        with open('./安徽省水利建设市场信用信息.txt', 'a+', encoding='utf-8') as f:
            f.write(line + "\n")
