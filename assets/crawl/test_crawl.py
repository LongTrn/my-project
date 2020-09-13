# from bs4 import BeautifulSoup as soup
# import pandas
# import requests
# import urllib.request as request
# import urllib.parse as parse

# # url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating%27' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
# url = 'https://www.kqxs.vn/' # các bạn thay link của trang mình cần lấy dữ liệu tại đây
# def get_page_content(url):
#   # page = requests.get(url, verify=False)
#   req = request.Request(url) 
#   resp = request.urlopen(req) 
#   respData = resp.read() 
#   return soup(respData.text,"html.parser")
# soup = get_page_content(url)

# # req = urllib.request.Request(url, data) 
# # resp = urllib.request.urlopen(req) 
# # respData = resp.read() 

# tables = soup.findAll('div', class_='miennam bggradient1')

# for each in tables:
#   print(each)


# # 
# # movies = soup.findAll('h3', class_='lister-item-header')

# # for each in movies:
# #   print(each,'\n')
# # print(movies)
# # titles = [movie.find('a').innerHTML for movie in movies]
# # print(titles,'\n')
# # release = [rs.find('span',class_="lister-item-year text-muted unbold").innerHTML for rs in movies]
# # print(release,'\n')
# # # rate = soup.findAll('div', 'inline-block ratings-imdb-rating')['data-value']
# # print(rate,'\n')
# # certificate = [ce.innerHTML for ce in soup.findAll('span',class_='certificate')]
# # print(certificate,'\n')
# # runtime = [rt.innerHTML for rt in soup.findAll('span',class_='runtime')]
# # print(runtime,'\n')
# # genre = [gr.innerHTML for gr in soup.findAll('span',class_="genre")]
# # print(genre,'\n')
# # rates = [rate['data-value'] for rate in soup.findAll('div',class_='inline-block ratings-imdb-rating')]
# # print(rates,'\n')

# # 
# # pandas.DataFrame({
# #   'titles':titles, 
# #   # 'release':release, 
# #   # 'certificate':certificate,
# #   # 'runtime':runtime,
# #   # 'genre': genre,
# # #   'rates': rates
# # })

'''

'''

# import scrapy
# class ExampleSpider1(scrapy.Spider):
#     name = 'examplespider1'
#     allowed_domains = ['www.familug.org']
#     start_urls = ['https://www.familug.org/search/label/Python',
#                   'https://www.familug.org/search/label/Command']

#     def parse(self, response):
#         self.logger.info('A response from {} just arrived'.format(response.url))
#         self.logger.debug('Nothing wrong in {}'.format(response.url))

# class ExampleSpider2(scrapy.Spider):
#     name = 'examplespider2'
#     allowed_domains = ['www.familug.org']
#     start_urls = ['https://www.familug.org/search/label/Python',
#                   'https://www.familug.org/search/label/Command']

#     def parse(self, response):
#         for title in response.css('h3.post-title.entry-title a::text').getall():
#             self.logger.info('Welcome' + title)
#             yield {'title': title}

#         for href in response.css('h3.post-title.entry-title a::attr(href)').getall():
#             yield scrapy.Request(href, self.parse)

'''
'''

