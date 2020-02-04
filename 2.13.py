from urllib import request
import urllib
import time

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}

def loadpage(fullurl, filename):
    print("正在下载:", filename)
    req = request.Request(fullurl,headers=header)
    resp = request.urlopen(req).read()
    return resp


def writepage(html, filename):
    print("正在保存:", filename)
    with open(filename,"wb") as f:
        f.write(html)

    print("------------------------------")


def tiebaSpider(url, begin, end):
    for page in range(begin, end+1):
        pn = (page-1)*50
        fullurl = url + "&pn=" + str(pn)
        filename = "d:/test/第"+str(page)+"页.html"
        html = loadpage(fullurl, filename)
        writepage(html, filename)


if __name__ == '__main__':
    kw = input("请输入贴吧名:")
    begin = int(input("请输入起始页:"))
    end = int(input("请输入结束页"))
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})
    url = url + key
    tiebaSpider(url, begin, end)