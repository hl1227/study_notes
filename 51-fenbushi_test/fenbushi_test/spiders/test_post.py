import scrapy
from scrapy_redis.spiders import RedisSpider


class HpbSpider (RedisSpider):
    name = 'hpb'
    redis_key = 'test_post_data'
    def make_request_from_data (self ,data) :
        return scrapy.FormRequest("https://www.httpbin.org/post",formdata={"data":data} ,callback=self.parse)
    def parse(self,response):
        print(response.body)
#scrapy crawl hpb