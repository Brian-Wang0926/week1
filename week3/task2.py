# https://www.ptt.cc/bbs/movie/index.html
# 標題、推文數、和發佈時間
# 發佈時 間必須是完整的格式，例如 Fri Jul 14 23:14:36 2023，完整發佈時間的資料，需進入文章連 結後取得。
# 連續爬取 3 頁的資料
# BeautifulSoup 
# 以一行一文章的格式，輸出到 movie.txt 中
# [新聞]影迷必朝聖5小時極致電影 文溫德斯直到世界,4,Fri Jul 14 23:34:43 2023 
# [問片] 恐龍電影,0,Sat Jul 15 00:01:14 2023

import urllib.request as req
import bs4
def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")

    data=root.find_all("div",class_="r-ent")
    print(len(data))
    for i in range(len(data)):
        if data[i].contents[3].contents[1] != None:
            if data[i].contents[1].contents[0].string == None:
                print(data[i].contents[3].contents[1].string,"0",sep=',')
            print(data[i].contents[3].contents[1].string,data[i].contents[1].contents[0].string,sep=',')

    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc/"+getData(pageURL)
    count+=1