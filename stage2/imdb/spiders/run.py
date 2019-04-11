# coding:utf-8


from scrapy import cmdline

cmdline.execute("scrapy crawl imdb -o imdb.json".split())
