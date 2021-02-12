# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class LotofacilPipeline(object):
    def __init__(self):
        self.create_connection()
        # self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root',
                                            passwd='',
                                            database='lottery')

        self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS megaSena""")
    #     self.curr.execute(
    #         """create table megaSena(id integer PRIMARY KEY AUTO_INCREMENT,name text,ticket_numbers text,entryDate text,contestNo text,est_next_contest text,five_final_contest text,jackpot_mega_draw text,next_contest_prize text,created_date text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into lotteryapp_lotofacil values (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item['est_next_contest'],
            item['entryDate'],
            item['contestNo'],
            item['created_date'],
            item['five_final_contest'],
            item['jackpot_mega_draw'],
            item['name'],
            item['next_contest_prize'],
            item['ticket_numbers'],

        ))
        self.conn.commit()
