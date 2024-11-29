# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiyeItem(scrapy.Item):

    # 企业名称
    company_name = scrapy.Field()
    # 法人代表
    corporate_representative = scrapy.Field()
    # 企业类型
    company_type = scrapy.Field()
    # 通讯地址
    address = scrapy.Field()
    # 综合评价
    overall_merit = scrapy.Field()
    # 统一社会信用代码
    social_code = scrapy.Field()
    # 评价年度
    overall_year = scrapy.Field()
    # 注册资金
    registered_capital = scrapy.Field()

