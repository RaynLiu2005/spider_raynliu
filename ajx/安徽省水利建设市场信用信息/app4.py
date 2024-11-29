import json
import time
import requests
import csv

# 定义API的URL模板
url_template = "http://61.190.26.79:5000/General/alljudge_json?page={}&limit=20&jtype=0&chnm=&apti=&result=&st=0"

# HTTP请求头
headers = {
    "Referer": "http://61.190.26.79:5000/Home/lstJUDGE",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

# 定义CSV文件的列名
fieldnames = ['id', 'unit_name', 'address', 'apti', 'score']

# 打开CSV文件以写入
with open('./安徽省水利建设市场信用信息.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # 写入表头

    # 遍历所有页面
    for number in range(1, 316):
        time.sleep(3)  # 延迟以避免过于频繁的请求
        url = url_template.format(number)

        try:
            res = requests.get(url, headers=headers)
            res.raise_for_status()  # 如果请求出错，这里会抛出异常
            data = json.loads(res.text)
            items = data.get('data', [])  # 使用get方法避免KeyError

            # 遍历每个项目并写入CSV
            for item in items:
                row = {
                    'id': item.get('ID'),
                    'unit_name': item.get('UNITNAME', '').replace("\r", "").replace("\n", "").replace("\t", "").replace(
                        " ", ""),
                    'address': item.get('ADDRESS', '').replace("\r", "").replace("\n", "").replace("\t", "").replace(
                        " ", ""),
                    'apti': item.get('APTI', ''),
                    'score': item.get('SCORE')
                }
                writer.writerow(row)  # 将数据写入CSV文件

        except requests.RequestException as e:
            print(f"请求错误: {e}")
        except json.JSONDecodeError as e:
            print(f"解析JSON错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")

print("数据抓取完成并写入CSV文件。")