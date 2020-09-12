import scrapy
import os

class LotterySpider(scrapy.Spider):
    name = "lottery"

    def start_requests(self):
        # urls = ['https://www.kqxs.vn/do-ket-qua/?date=11-09-2020']
        # link = 'https://www.kqxs.vn/do-ket-qua/?date='
        # start = '01-08-2020/'
                
        # for i in range(1,32):
        #     j = str(i)
        #     if i < 10: j = '0' + j
        #     date = start.split('-')
        #     date[0] = j
        #     start = '-'.join(date)
        #     page = start
        #     tmp = link + page
        #     urls.append(tmp)
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

        urls = [
            'http://localhost/X%e1%bb%95%20s%e1%bb%91%20-%20XS%20m%e1%bb%9bi%20nh%e1%ba%a5t,%20ch%c3%adnh%20x%c3%a1c%20nh%e1%ba%a5t!%20%e2%80%93%20KQXS.VN.html',
            # 'https://www.kqxs.vn/do-ket-qua/?date=11-09-2020',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
            # Storeing source code of page
            Path = '\\'.join(os.path.dirname(os.path.realpath(__file__)).split('\\')[:-2])
            page = response.url.split("/")[-1].split('=')[-1]
            filename = 'lottery-%s.html' % page
            filename = os.path.join(Path, filename)   
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            self.log('Saved file' + str(response.css('div.kq table tbody').getall()))
            self.log('Saved file' + str(response.css('div.kq table tbody tr td:last-child::text').get()))
        '''
        listNums = []
        for tables in response.css('div.kq table'):
            for table in tables.css('tbody'):
                for cell in table.css('tr'):
                    '''
                        return tung gia tri type str vao file
                        key = cell.css('td::text').get()
                        yield{
                            # key: cell.css('td:last-child::text').re('[^\s-][\d]*')
                            key: cell.css('td:last-child::text').re('[^\s-][\d]*')
                        }
                    '''
                    num = cell.css('td:last-child::text').re('[^\s-][\d]*')
                    listNums.append(num)
        listNums.remove([])
        listNums = [int(num) for listNum in listNums for num in listNum]
        listNums.sort()
        setNums = {}
        setNums.setdefault('nums',listNums)
        yield setNums                    
            
            
'''
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
'''
    