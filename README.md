# BFS (Bookmark Full-Text Search) 書籤全文搜尋器

# 安裝教學

## Windows

### 安裝python
至 https://www.python.org/ 下載python安裝檔
安裝時記得把設為環境變數打勾

### 下載 ckip model
1. 開一個文件，輸入以下程式碼
```
# -*- coding: utf-8 -*-
from ckiptagger import data_utils
data_utils.download_data_gdown("./")
```
2. 存擋為ckip_download.py
3. 執行python ckip_download.py

### Install python packages using virtualenv
#### Create and activate virtualenv
```
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```
#### Install required packages
```
pip install -r requirements.txt
```

### Load extension for Chrome
* Settings->Extensions->turn on Developer mode
* Load unpacked->select file "manifest.json"->done

## Run Server
```
cd server
python bfs.py
```

## References
* Building Search Engines with Gensim: https://christop.club/talks/tripython_2015/#/
* Debounce: https://github.com/lishengzxc/bblog/issues/7
* [mozilla-JavaScript-APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
