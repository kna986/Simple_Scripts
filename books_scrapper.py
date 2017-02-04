# -*- coding: utf-8 -*-
import bs4 as bs
from urllib.request import Request, urlopen

'''
Not very fast, but very simple script for books scrapping for http://book-online.com.ua
'''

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3, windows-1251',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive'
}

pages = 1

while pages != 229:  # Change number of pages in current book
    url_site = 'http://book-online.com.ua/read.php?book=5065&page=' + str(pages)    # In url change book=5065 on your book
    req = Request(url_site, headers=hdr)
    sauce = urlopen(req).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    tags = soup.find("div", id="ptext")
    print(tags.text)
    pages += 1
