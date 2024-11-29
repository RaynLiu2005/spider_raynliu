import json
import requests

url = "https://hwdms.mot.gov.cn/BMWebSite/evaluate/getEvaluateList.do"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
text = json.loads(res.text)
all_items = text['rows']
for item in all_items:
    corpName = item['corpName']
    creditCode = item['creditCode']
    companytype = item['companyType']
    oeriodCode = item['oeriodCode']  # 注意这里的字段名可能是 periodCode 而不是 oeriodCode
    evaGrade = item['evaGrade']
    doScore = item['doScore']
    print(corpName, creditCode, companytype, oeriodCode, evaGrade, doScore)