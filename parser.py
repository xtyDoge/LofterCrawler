from bs4 import BeautifulSoup

class LofterParser():
    """
    解析Lofter页面，获取接下来应爬取的url与应爬取图片的url
    """
    @classmethod
    def getImgPageHref(cls,response):
        """
        获取图片应有的连接-一个主贴中
        """
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        pageHrefs = []
        for col in soup.select('.photo .img'):
            try:
                pageHrefs.append(col.select('a')[0]['href'])
            except Exception as e:
                print('Not a PhotoPage')
        return pageHrefs            
        # TODO 用decorator加入打印日志功能？

    @classmethod
    def getImgHref(cls,response):
        """
        获取高清图片地址
        """
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        imgHrefs = []
        for post in soup.select('.img'):
            if post.select('.imgclasstag'):
                imgHrefs.append(post.select('.imgclasstag')[0]['bigimgsrc'])
        return imgHrefs

    @classmethod
    def getUserpageHref(cls,response):
        """
        获取点赞人的主页超链接
        """
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        userHrefs = []
        for note in soup.select('.note.share'):
            userHrefs.append(note.select('a')[0]['href'])
        return userHrefs



# def main():


# if __name__ == '__main__':
#     main()