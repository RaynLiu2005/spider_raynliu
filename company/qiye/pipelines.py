# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymysql


class MYSQLPipeline:
    def open_spider(self, spider):
        host = spider.settings.get("MYSQL_HOST")
        db = spider.settings.get("MYSQL_DB")
        user = spider.settings.get("MYSQL_USER")
        pwd = spider.settings.get("MYSQL_PWD")
        self.conn = pymysql.connect(host=host, db=db, user=user, password=pwd)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = ("insert into job(social_code, company_name, address, "
               "corporate_representative, company_type, overall_merit) "
               "values (%s, %s, %s, %s, %s, %s)")
        try:
            self.cursor.execute(sql, (item['social_code'], item['company_name'],
                                      item['address'], item['corporate_representative'],
                                      item['company_type'], item['overall_merit']
                                      ))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"Error inserting data: {e}")
        return item
