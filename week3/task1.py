
# 要求一:Python 取得網路上的資料並儲存到檔案中 台北市政府提供景點公開資料連線網址如下:
# https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json
# 請撰寫一隻 Python 程式，能從以上網址取得資料，並按照以下要求輸出成兩個 CSV 格式的 檔案:
# 1. 將景點資料用一行一景點的形式，輸出到 attraction.csv 的檔案。特別注意，輸出的資 料中，只取第一張圖檔的網址。
# 2. 將景點資料以鄰近的捷運站分群，一行一捷運站的形式，輸出到 mrt.csv 的檔案。
# 請將生成的 attraction.csv 以及 mrt.csv 檔案包含在你的任務資料夾中。不可以使用任何第三方套件，例如 Pandas、Requests 等等。
# 提醒:區域資料請參考原始資料的地址欄位，必須是三個字，並且為以下區域的其中一個:中正區、萬華區、中山區、大同區、大安區、松山區、
# 信義區、士林區、文山區、北投區、內湖區、南港區內湖區、南港區。

# attraction.csv 的資料格式
# attraction.csv 的資料範例
# 景點名稱[stitle],區域[address](篩選區域成三個字),經度[longitude],緯度[latitude],第一張圖檔網址[file] (第一張圖片)
# 捷運站名稱,景點名稱一,景點名稱二,景點名稱三,...
import urllib.request as request
import json
import csv
address_lists=["中正區","萬華區","中山區","大同區","大安區","松山區","信義區","士林區","文山區","北投區","內湖區","南港區","內湖區","南港區"]
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
with open("attraction.csv","w",newline="") as file:
    writer=csv.writer(file)
    for item in clist:
        def add(address_lists):
            for address_list in address_lists: #篩選地址中包含地址清單的文字，並列印出來 
                if address_list in item["address"]:
                    return address_list
        first_pic=item["file"][0:item["file"].lower().find('.jpg')+4]
        writer.writerow([item["stitle"],add(address_lists),item["longitude"],item["latitude"],first_pic])

# 找出相同mrt，並印出對應stitle
with open("mrt.csv","w",newline="") as file:
    writer=csv.writer(file)
    mrt_list=[] # 找出所有不重複的捷運站 str
    same_mrt_stitle=[] # 找出相同捷運站的景點 list
    for mrt in clist:
        if mrt["MRT"] not in mrt_list:
            mrt_list.append(mrt["MRT"])

    for mrt in mrt_list:
        for data in clist:
            if data["MRT"] == mrt:
                same_mrt_stitle.append(data["stitle"])
        same_mrt_stitle.insert(0,mrt)
        writer.writerow(same_mrt_stitle)
        same_mrt_stitle.clear()
