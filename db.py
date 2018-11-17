import redis
from conf import *

class RedisClient():
    """
    为连接数据库提供封装的方法
    """
    def __init__(self,type,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """
        Redis数据库实例初始化
        host，port，password分别为地址，端口，密码
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password)
        pass

    def get(self):
        pass

    def set(self):
        pass

    def delete(self):
        pass



class UrlDbClient(RedisClient):
    """
    连接Redis数据库，派生于DBClient
    """
    
    def listUnCrawled(self):
        """
        列出未被爬取的url
        """
        return []

