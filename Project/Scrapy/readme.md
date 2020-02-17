### pip install scrapy

scrapy startproject postcrape

scrapy crawl posts  #posts name mentioned in file

scrapy shell https://blog.scrapinghub.com

response.css('title')
response.css('title').get()
response.css('title::text').get()
response.css('h3::text').get()
response.css('h3::text')[1].get()
response.css('h3::text').getall()
response.css('p::text').re(r'(\w+) you (\w+)')
response.xpath('//h3')
response.xpath('//h3/text()')
response.xpath('//h3/text()').extract()
response.xpath('//h3/text()').getall()
post=response.css('div.post-item')[0]
post
title=post.css('.post-header h2 a::text')[0].get()
title
date=post.css('.post-header h2 a::text')[1].get()
date
author=post.css('.post-header h2 a::text')[2].get()

for post in response.css('div.post-item'):
    title=post.css('.post-header h2 a::text')[0].get()
    date=post.css('.post-header h2 a::text')[1].get()
    author=post.css('.post-header h2 a::text')[2].get()
    print(dict(title=title,date=date,author=author))
    
    
