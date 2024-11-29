from bs4 import BeautifulSoup
import requests
import csv


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None


def scrape_company_ratings(html):
    # 解析HTML内容
    soup = BeautifulSoup(html, 'html.parser')

    # 定位到包含数据的div
    new_all_box = soup.find('div', class_='newAll_box')

    # 初始化一个空列表来存储结果
    companies = []

    # 遍历所有的a标签
    for a_tag in new_all_box.find_all('a'):
        # 获取公司名称（假设是第二个li标签，注意检查实际的HTML结构）
        company_name_li = a_tag.find_all('li')
        if len(company_name_li) > 1:
            company_name = company_name_li[1].text.strip()
            # 获取评级（假设是第三个li标签，注意检查实际的HTML结构）
            if len(company_name_li) > 2:
                rating = company_name_li[2].text.strip()
                # 将公司名称和评级添加到列表中
                companies.append({'company_name': company_name, 'rating': rating})

                # 返回结果列表
    return companies


def save_to_csv(data, filename='四川信用交通1.csv'):
    fieldnames = ['id', 'company_name', 'rating']
    with open(filename, mode='w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        for index, company in enumerate(data, start=1):
            writer.writerow({'id': index, 'company_name': company['company_name'], 'rating': company['rating']})


def main():
    base_url = 'http://182.150.21.186:8080/jsscplatemore-good-'
    all_companies = []

    for page_num in range(1, 12):  # 范围是1到11，包括11
        url = f"{base_url}{page_num}"
        html = get_html(url)
        if html:
            companies = scrape_company_ratings(html)
            all_companies.extend(companies)  # 使用extend将列表合并

    if all_companies:
        save_to_csv(all_companies)
        print("所有数据已保存至CSV文件。")
    else:
        print("未找到任何公司数据。")


if __name__ == '__main__':
    main()
