import requests
import json
import csv


def get_html(url, page):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        }
        data = {'page': page}
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f'请求网页异常，页面: {page}', e)
        return None


def parser(json_text):
    txt = json.loads(json_text)
    for item in txt:
        corpName = item['corpName']
        creditCode = item['creditCode']
        companytype = item['companyType']
        oeriodCode = item['oeriodCode']  # 注意这里的字段名可能是 periodCode 而不是 oeriodCode
        evaGrade = item['evaGrade']
        doScore = item['doScore']


if __name__ == "__main__":
    base_url = "https://hwdms.mot.gov.cn/BMWebSite/evaluate/getEvaluateList.do"
    all_data = []

    # 遍历所有页面
    for page in range(1, 732):  # 根据实际情况调整页数范围
        json_text = get_html(base_url, page)
        if json_text:
            page_data = parser(json_text)
            all_data.extend(page_data)

            # 将数据保存到CSV文件
    csv_filename = '全国公路建设市场信用信息管理.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # 假设每个条目都是一个字典，并且所有条目的键都相同
        if all_data:
            fieldnames = all_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()  # 写入表头
            writer.writerows(all_data)  # 写入数据行

    print(f"总共获取了{len(all_data)}条数据，并已保存到{csv_filename}文件中")