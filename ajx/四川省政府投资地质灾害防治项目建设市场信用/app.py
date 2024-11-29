import json
import time
import requests
import csv

url = "http://zxpt.scdzfz.cn:17085/api/unitCreditList?page={}&limit=20&unitName=&unitType="

headers = {
    "Referer": "http://zxpt.scdzfz.cn:17085/credit/index?page=xinyongpingjia",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# 定义CSV文件的列名
fieldnames = ['unit_name', 'credit_rating', 'credit_score', 'rating_time']

# 打开CSV文件，并写入表头
with open('./四川省政府投资地质灾害防治项目建设市场信用.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 爬取数据并写入CSV文件
    for number in range(1, 22):
        time.sleep(1)

        res = requests.get(url.format(number), headers=headers)
        data = json.loads(res.text)
        items = data['data']

        for item in items:
            row = {
                'unit_name': item.get('unitName'),
                'credit_rating': item.get('creditRating'),
                'credit_score': item.get('creditScore'),
                'rating_time': item.get('ratingTime')
            }
            writer.writerow(row)  # 将数据写入CSV文件