import requests
from urllib.parse import urlparse
from hashlib import md5
import os


class PhotoDownloader():
    """
    从数据库中爬取的图片url来下载
    """
    @classmethod
    def saveFile(cls, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        }
        dirPath = 'pictures'
        session = requests.Session()
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
            print('we has make the dir')
        try:
            response = session.get(url, headers=headers)
            file_path = '{0}/{1}.{2}'.format(dirPath, md5(response.content).hexdigest(),'jpg')
            
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('This File Already Exist')

        except requests.ConnectionError:
            print('Failed to Download File.')


# def main():
    
#     pd = photoDownloader()
#     url = 'http://imglf4.nosdn0.126.net/img/MXdQYndpb1JqNGoxTzVKWWN6aExFWHBpNEw4UHZ5T2JpcWFSOHdXVldvSEpiVUlObjN6c1lRPT0.jpg?imageView&thumbnail=1680x0&quality=96&stripmeta=0&type=jpg'
#     pd.saveFile(url)
# if __name__ == '__main__':
#     main()