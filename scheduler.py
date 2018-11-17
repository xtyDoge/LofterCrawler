from crawler import LofterCrawler
from parser import LofterParser
from downloader import PhotoDownloader
import threading

def main():

    ACCU = 0

    lofterCrawler = LofterCrawler()
    content = lofterCrawler.getSeedPage()
    hrefs = LofterParser.getImgPageHref(content)
    for href in hrefs:

        content = lofterCrawler.getPageByUrl(href)
        # 获取到的图片下载链接
        sharedHrefs = LofterParser.getUserpageHref(content)
        imgHrefs = LofterParser.getImgHref(content)
        print('**************')
        print('开始下载URL:%s，共%d张图片' %(href,len(imgHrefs)))
        
        threadingList = []
        for idx,ih in enumerate(imgHrefs):
            threadingList.append(threading.Thread(target=PhotoDownloader.saveFile,args=(ih,)))
            ACCU += 1
            print('已保存，进度%d/%d，共计%d' % (1+idx,len(imgHrefs),ACCU))
        for thr in threadingList:
            thr.start()
        thr.join()

    # 爬取其他博主的连接

    for shared in sharedHrefs:
        print('开始爬取博主'+shared)
        content = lofterCrawler.getUserPage(shared)
        hrefs = LofterParser.getImgPageHref(content)
        for href in hrefs:
            content = lofterCrawler.getPageByUrl(href)
            # 获取到的图片下载链接
            sharedHrefs = LofterParser.getUserpageHref(content)
            imgHrefs = LofterParser.getImgHref(content)
            print('**************')
            print('开始下载URL:%s，共%d张图片' %(href,len(imgHrefs)))

            threadingList = []
            for idx,ih in enumerate(imgHrefs):
                threadingList.append(threading.Thread(target=PhotoDownloader.saveFile,args=(ih,)))
                ACCU += 1
                print('已保存，进度%d/%d，共计%d' % (1+idx,len(imgHrefs),ACCU))
            for thr in threadingList:
                thr.start()
            thr.join()



    print('下载完毕')

if __name__ == '__main__':
    main()