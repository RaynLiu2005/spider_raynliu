import scrapy
from qiye.items import QiyeItem


class info3Spider(scrapy.Spider):
    name = "info3"
    allowed_domains = ["xy.scjtxxh.cn"]
    start_urls = [f"http://xy.scjtxxh.cn:8080/dlysplatemore-mid-{i}" for i in range(1, 297)]

    def parse(self, response, **kwargs):
        for row in response.xpath('//*[@class="newAll_box"]/a'):
            url = row.xpath('@href').get()
            yield scrapy.Request(
                url='http://xy.scjtxxh.cn:8080'+url,
                callback=self.parse_detail
            )

    def parse_detail(self, response):
        item = QiyeItem()
        for row in response.xpath('//*[@class="gridtable"]/tbody'):
            item['company_name'] = row.xpath('./tr[1]/td[2]/text()').get()
            item['social_code'] = row.xpath('./tr[2]/td[2]/text()').get()
            item['corporate_representative'] = row.xpath('./tr[3]/td[2]/text()').get()
            item['address'] = row.xpath('tr[8]/td[2]/text()').get()
            item['company_type'] = row.xpath('tr[7]/td[2]/text()').get()
            item['overall_merit'] = row.xpath('/html/body/div/section[2]/div[1]/span[2]/strong/text()').get()
            item['overall_year'] = row.xpath('./tr[4]/td[2]/text()').get()
            item['registered_capital'] = 0
            yield item
