# -*- coding: utf-8 -*-
import scrapy
from fenghuang.items import FenghuangItem
class FengSpider(scrapy.Spider):
    name = 'feng'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/ipad']
    def parse(self, response):
        #首页
        #所有标题和链接
        titles = response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
        links = response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
        #文字标题和链接对应的内容
        for title, link in zip(titles, links): #遍历获取每一个标题和相对应的链接
            # 记录  标题 以及 标题链接
            # title link
            data = {'title': title, 'link': link}
            # 请求分类页面
            yield scrapy.Request(link, meta={'data': data}, callback=self.newlist)
            #上面一步中，meta是传递数据，callback返回到函数getNewList
    def newlist(self, response): #请求
        data = response.meta['data'] #将上面的函数传递下来
        title = data["title"]  #定义此时的title
        link = data['link']   #定义此时的link
        biaotis = []  #定义两个空数组，分别放置每一类的标题和链接2
        biaotilianjies = []
        if title == "资讯首页":  #如果标题等于国际 获取国际这一类linkd下的标题和链接2
            biaotis += response.xpath("//div[@class='left_co1']/div[@class='tit']/h2/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='left_co1']/div[@class='tit']/h2/a/@href").extract()
        elif title == "即时":  #同上
            biaotis += response.xpath("//div[@class='newsList']/ul/li/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='newsList']/ul/li/a/@href").extract()
        elif title == "大陆":
            biaotis += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        elif title == "国际":  #如果标题等于国际 获取国际这一类linkd下的标题和链接2
            biaotis += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        elif title == "台湾":
            biaotis += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        elif title == "军事":
            biaotis += response.xpath("//div[@class='news-34dpVmYc']/h1[@class='newsFirstTitle-2Bj_hE7a']/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='news-34dpVmYc']/h1[@class='newsFirstTitle-2Bj_hE7a']/a/@href").extract()
        elif title == "社会":  #同上
            biaotis += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
        elif title == "图片":
            biaotis += response.xpath("//div[@class='listItem-2oY_PArX']/h3/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='listItem-2oY_PArX']/h3/a/@href").extract()
        elif title == "评论":  #如果标题等于国际 获取国际这一类linkd下的标题和链接2
            biaotis += response.xpath("//div[@class='topNews-2BQWVUtl']/h3[@class='second_title-1QD9gZws top_news_title']/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='topNews-2BQWVUtl']/h3[@class='second_title-1QD9gZws top_news_title']/a/@href").extract()
        elif title == "历史":
            biaotis += response.xpath("//li[@class='news-stream-newsStream-news-item-has-image clearfix news_item']/div[@class='news-stream-newsStream-news-item-infor']/h2/a/text()").extract()
            biaotilianjies += response.xpath("//li[@class='news-stream-newsStream-news-item-has-image clearfix news_item']/div[@class='news-stream-newsStream-news-item-infor']/h2/a/@href").extract()
        elif title == "文化":
            biaotis += response.xpath("//li[@class='news-stream-newsStream-news-item-has-image clearfix news_item']/div[@class='news-stream-newsStream-news-item-infor']/h2/a/text()").extract()
            biaotilianjies += response.xpath("//li[@class='news-stream-newsStream-news-item-has-image clearfix news_item']/div[@class='news-stream-newsStream-news-item-infor']/h2/a/@href").extract()
        elif title == "国学":  #同上
            biaotis += response.xpath("//ul[@class='news-stream-basic-news-list']/li/a/text()").extract()
            biaotilianjies += response.xpath("//ul[@class='news-stream-basic-news-list']/li/a/@href").extract()
        elif title == "智库":
            biaotis += response.xpath("//div[@class='newsItem-3D2ASUVg']/h1/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='newsItem-3D2ASUVg']/h1/a/@href").extract()
        elif title == "专题":  #如果标题等于国际 获取国际这一类linkd下的标题和链接2
            biaotis += response.xpath("//div[@class='box632_b']/div[@class='newsList']/ul/li/a/text()").extract()
            biaotilianjies += response.xpath("//div[@class='box632_b']/div[@class='newsList']/ul/li/a/@href").extract()
        elif title == "排行":
            biaotis += response.xpath("//table/tr/td/h3/a/text()").extract()
            biaotilianjies += response.xpath("//table/tr/td/h3/a/@href").extract()
        if biaotis and biaotilianjies: #如果标题和链接2存在
            for biaoti, biaotilianjie in zip(biaotis, biaotilianjies):  #遍历所有标题和标题链接
                item = FenghuangItem()   #new实例化item
                item['title'] = title    #
                item['link'] = link
                item['biaoti'] = biaoti
                item['biaotilianjie'] = biaotilianjie
                # yield item   #请求
                yield scrapy.Request(biaotilianjie, meta={'item': item}, callback=self.getNewCon)
                # 返回请求信息，连接管道 meta传递数据，callback返回到函数getNewCon
    def getNewCon(self, response): #请求
        item = response.meta['item'] #将上面的函数传递下来
        biaoti = item["biaoti"]  #定义此时的title
        biaotilianjie = item['biaotilianjie']   #定义此时的link
        neirongs = []  #定义两个空数组，分别放置每一类的标题和链接2
        times = []
        if biaoti and biaotilianjie:
            times += response.xpath("//p[@class='p_time']/span/text()").extract()
            neirongs += response.xpath("//div[@id='main_content']/p/text()").extract()
        for time,neirong in zip(times,neirongs):
            iteme = FenghuangItem()   #new实例化iteme
            iteme['time'] = time
            iteme['neirong'] = neirong
            yield iteme

                


