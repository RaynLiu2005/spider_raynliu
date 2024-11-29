# 公交建设
import scrapy
from qiye.items import QiyeItem


class info2Spider(scrapy.Spider):
    name = "info2"
    allowed_domains = ["xy.scjtxxh.cn"]
    start_urls = [f"http://xy.scjtxxh.cn:8080/jsscplatemore-mid-{i}" for i in range(1,461)]

    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="newAll_box"]/a'):
            url = row.xpath('@href').get()
            yield scrapy.Request(
                url='http://xy.scjtxxh.cn:8080'+url,
                callback=self.parse_detail
            )

    def parse_detail(self,response):
        item = QiyeItem()
        for row in response.xpath('//*[@class="gridtable"]/tbody'):
            item['company_name'] = row.xpath('./tr[2]/td[2]/text()').get()
            item['social_code'] = row.xpath('./tr[3]/td[2]/text()').get()
            item['corporate_representative'] = row.xpath('./tr[5]/td[2]/text()').get()
            item['address'] = row.xpath('tr[9]/td[2]/text()').get()
            item['company_type'] = row.xpath('tr[7]/td[2]/text()').get()
            item['overall_merit'] = row.xpath('tr[10]/td[2]/text()').get()
            item['registered_capital'] = row.xpath('./tr[4]/td[2]/text()').get()
            item['overall_year'] = row.xpath('//*[@class="company_level"]/span[3]/strong/text()').get()
            yield item

