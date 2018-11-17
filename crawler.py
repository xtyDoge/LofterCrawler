import requests
import re

class Crawler(object):
    """
    爬取类
    """
    def __init__(self,seedUrl):
        """
        初始化seedURL，headers，session
        """
        self.seedUrl = seedUrl
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7',
            'Host':'hiroron.lofter.com',
            'Connection':'keep-alive',
            'Referer': 'http://hiroron.lofter.com/',
        }
        self.session = requests.Session()


    def getPageByUrl(self,url,type='GET'):
        """
        按照url爬取页面
        """
        try:
            if type == 'GET':
                response = self.session.get(url,headers=self.headers)
            elif type == 'POST':
                response = self.session.post(url,headers=self.headers)
            else:
                raise Exception('You can just give type GET or POST')

            if response.status_code == 200:
                return response
            else:
                print("GET with status code" + str(response.status_code))
        except requests.RequestException as re:
            print(re)

    def changeHeaders(self,headers):
        """
        针对不同用户更换不同Headers
        """
        self.headers = headers



class LofterCrawler(Crawler):
    """
    具体Lofter的爬虫
    """
    
    def __init__(self):
        return super().__init__(seedUrl="http://hiroron.lofter.com/")

    def getSeedPage(self):
        """
        获取种子Url的页面
        """
        print('已经爬取种子界面:%s' % 'http://hiroron.lofter.com/')
        return self.getPageByUrl(self.seedUrl)

    def getUserPage(self,url):
        """
        获取新用户的首页内容
        """
        # 更换请求头
        usernameRe = re.compile(r'\/\/(.*?)\.lofter\.com')
        usr = usernameRe.search(url).group(1)
        headers = self.headers
        headers['Host'] = usr + '.lofter.com'
        headers['Referer'] = url
        self.changeHeaders(headers)
        # 请求
        return self.getPageByUrl(url)


if __name__ == '__main__':
    lc = LofterCrawler()
    url = 'http://anmaoxuezi.lofter.com/'
    print(lc.getUserPage(url).text)