import scrapy
import json
from qiye.items import QiyeItem


class Info1Spider(scrapy.Spider):
    name = "info1"
    allowed_domains = ["wtis.mot.gov.cn"]
    start_urls = [f"https://wtis.mot.gov.cn/motcreditservice/qyregisterinfo/getQyRegisterInfoList?limit=10&start={i}" for i in range(1, 129)]

    def parse(self, response, **kwargs):
        data = json.loads(response.text)
        item = QiyeItem()
        for i in data['DATA']:
            item['social_code'] = i["CREDIT_CODE"]
            item['company_name'] = i["CORP_NAME"]
            item['corporate_representative'] = i["LEGAL_REPRESENTATIVE"]
            item['address'] = i["REG_CITY_CODE"]
            item['company_type'] = i["CORP_TYPE"]
            item['overall_merit'] = i["APTITUDE_TYPE"]
            yield item
