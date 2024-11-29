import json
import time
import requests
import csv
from lxml import etree
import re


def get_html(url, page):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "cookie": "JSESSIONID=495EB112CDEBF0AC15078968BFE342A7",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }
    try:
        data = {'page': page}
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response.encoding = "UTF-8"
        return response.text
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        return None


def parse_detail_page(html):
    try:
        doc = etree.HTML(html)
        legal_representative = re.findall(re.compile(r'法定代表人：.*?<a .*?>(.*?)</a>', re.S), html)
        registered_capital = re.findall(re.compile(r'注册资本：.*?<span .*?>(.*?)</span>', re.S), html)
        address = re.findall(
            re.compile(r'地址：.*?<span .*?>.*?<span.*?>.*?<span.*?>.*?<span.*?>.*?<span.*?>(.*?)</span>', re.S), html)

        return (legal_representative[0] if legal_representative else "无",
                registered_capital[0] if registered_capital else "无",
                address[0] if address else "无")
    except Exception as e:
        print(f"Error parsing detail page: {e}")
        return ("无", "无", "无")


def xpath(html):
    try:
        data = json.loads(html)
        rows = data.get('rows', [])
        result_list = []

        for row in rows:
            base_info = [
                row.get('corpName', ''),
                row.get('companyType', ''),
                row.get('periodCode', ''),  # 注意这里可能是'periodCode'而不是'oeriodCode'
                row.get('creditCode', ''),
                row.get('evaGrade', ''),
                row.get('doScore', '')
            ]

            detail_url = f"https://www.qcc.com/web/search?key={base_info[0]}"
            detail_headers = {

                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.8121 SLBChan/111 SLBVPV/64-bit",
                "Cookie": "QCCSESSID=587ada5f4981bda628943820fa; qcc_did=bd8517ba-ee54-4fd3-8196-439d505e6117; UM_distinctid=192be676b411835-0f85fc52ec5193-26011951-172698-192be676b422702; CNZZDATA1254842228=406809527-1729771302-%7C1729775404; acw_tc=0a47308417297762485598706e00828a6e43c653ad7741cdb244bd761b07fa; tfstk=fCMK62xnUFY3UPSO6_OgZjt7ncKMiYnUx2ofEz4hNV3tcm73NWYUyf3S7W4Ie0W8V0gyYzxesDoUU8TDo8pmYDrsbj7DmW_1fcrdRNxyu7oUU8Tgvxi2bDubt0uxd8tTCuE7V8a7OOtTxuy5d76C1Naa5zw7O9Z_5urRO_aCFhn_7ue7Pb5XHzRuyThP4pVwWiPRFTMBUWaAdPqaXAL8trnICT6WGkFLlDa9uhn3s5izwYSPe7mIg4rjRwT8zAnsdjgXS64IMunmwqtlTlV-LRUSdKSY5vn-BWlGR6ZYpyFjdVs2mcFS6AendU5qjcUQMRcM_eVup2h4uWOw74nT-4ML1wLgrjmid53XSO3zwbM3CvT6HgkmnxIDaZ4Yq6t9X_5zOluXkcR1Xjfr8lUDjzfPa5cYXrx9X_5zOlrTohXOa_PiM"
            }


            detail_response = requests.get(detail_url, headers=detail_headers)
            detail_html = detail_response.text

            legal_rep, registered_capital, address = parse_detail_page(detail_html)

            result_list.append(base_info + [legal_rep, registered_capital, address])
            print(result_list)

        return result_list
    except Exception as e:
        print(f"Error processing JSON: {e}")
        return []


def save(out_list, file):
    with open(file, "a+", encoding="UTF-8", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(out_list)


if __name__ == "__main__":
    url = "https://hwdms.mot.gov.cn/BMWebSite/evaluate/getEvaluateList.do"
    for page in range(1, 731):  # 修改了页面范围以进行测试
        time.sleep(1)
        html = get_html(url, page)
        if html:
            print(f"第{page}页爬取成功")
            result = xpath(html)
            save(result, "ChatTTS-main/全国公路建设市场信用信息管理.csv")
        else:
            print(f"第{page}页爬取失败")
    print("保存成功")