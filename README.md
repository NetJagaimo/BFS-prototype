# BFS (Bookmark Full-Text Search) 書籤全文搜尋器

# 安裝教學

## 先下載這份原始碼

## 安裝python (windows才需要)
至 https://www.python.org/ 下載python安裝檔
安裝時記得把設為環境變數打勾

## 安裝python套件
### 創建並啟動virtualenv
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```
### 安裝所需套件
```
pip install -r requirements.txt
```

## 下載 ckip model
1. 開一個文件，輸入以下程式碼
```
# -*- coding: utf-8 -*-
from ckiptagger import data_utils
data_utils.download_data_gdown("./")
```
2. 存擋為ckip_download.py
3. 執行python ckip_download.py
4. 將下載下來的data.zip解壓縮到server資料夾裡面

## 啟動後端程式
```
cd server
python bfs.py
```

## 載入Chrome擴充套件
* 設定->擴充套件->將開發人員模式打開
* 載入未封裝項目->選擇bfs資料夾->完成
* 載入後會自動將書籤資料傳給後端程式進行資料爬取以及LSI模型建立，請等他完成
* 看到build model done就代表完成了

## 使用說明
在網址列輸入bfs加上空格，然後輸入欲查詢的關鍵字，不需要按enter，輸入完後即會將查詢結果顯示於網址列中

# 參考來源
* Building Search Engines with Gensim: https://christop.club/talks/tripython_2015/#/
* Debounce: https://github.com/lishengzxc/bblog/issues/7
* [mozilla-JavaScript-APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
