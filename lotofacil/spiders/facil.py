# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.keys import Keys
from scrapy.http import Request
import datetime
from selenium.webdriver.common.keys import Keys
import time
from ..items import LotofacilItem

class FacilSpider(scrapy.Spider):
    name = 'facil'
    allowed_domains = ['http://loterias.caixa.gov.br/']
    start_urls = ['http://loterias.caixa.gov.br/']

    def start_requests(self):
        yield SeleniumRequest(
            url='http://loterias.caixa.gov.br/',
            wait_time=15,
            screenshot=True,
            callback=self.parse
        )
    def parse(self, response):
        # img=response.meta['screenshot']
        # with open('screenshot.png','wb') as f:
        #     f.write(img)
        driver=response.meta['driver']
        driver.set_window_size(1024, 6000)
        data_link=driver.find_element_by_xpath("//*[@id='layoutContainers']/div[2]/div[1]/div/section/div[2]/div[2]/div[2]/div[2]/p[2]/a")
        # data_link.send_keys(Keys.ENTER)
        data_link.click()

        html=driver.page_source
        response_obj=Selector(text=html)
        driver.save_screenshot("inside.png")
        numbers=response_obj.xpath("//ul[@class='simple-container lista-dezenas lotofacil']/li")
        list_elements=[]
        for x in numbers:
            link=x.xpath("./text()").extract_first().split(' ')[40]
            list_elements.append(link)
            yield {"numbers":list_elements}
        ticket_number=str(list_elements).split('[')[1].split("]")[0]
        name=response_obj.xpath("//div[@class='content-hero gray-hero bottom-image']/h1/text()").extract_first()
        entryDate=response_obj.xpath("//span[@class='ng-binding']/text()").extract_first().split('(')[1].split(')')[0]
        contestNo=response_obj.xpath("//span[@class='ng-binding']/text()").extract_first().split(' ')[1].split('\n')[0]
        est_next_contest = response_obj.xpath("//div[@class='next-prize clearfix']/p/text()").extract_first().split(' ')[41]
        five_final_1st = response_obj.xpath("//p[@class='value ng-binding']/text()").extract_first().split(' ')[36]
        five_final_2nd = response_obj.xpath("//p[@class='value ng-binding']/text()").extract_first().split(' ')[37]
        five_final_contest = five_final_1st + five_final_2nd
        jackpot_mega_draw = response_obj.xpath("//span[@class='value ng-binding']/text()").extract_first()
        next_contest1 = response_obj.xpath("//p[@class='value ng-binding']/text()").extract_first().split(' ')[36]
        next_contest2 = response_obj.xpath("//p[@class='value ng-binding']/text()").extract_first().split(' ')[37]
        next_contest_prize=next_contest1 + next_contest2
        created_date=datetime.datetime.now()
        items = LotofacilItem()
        items['name'] = name
        items['ticket_numbers'] =ticket_number
        items['entryDate'] = entryDate
        items['contestNo'] = contestNo
        items['est_next_contest'] = est_next_contest
        items['five_final_contest'] = five_final_contest
        items['jackpot_mega_draw'] = jackpot_mega_draw
        items['next_contest_prize'] = next_contest_prize
        items['created_date'] = created_date

        yield items
