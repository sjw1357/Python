#coding:utf-8
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from var_dump import *


excel_name = 'books.xlsx'
wb = Workbook()
ws1 = wb.active
ws1.title = 'first'

def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    }
    html = requests.get(url=url, params=None, headers=headers)
    return html.content

def get_con(html):
    soup = BeautifulSoup(html, 'html.parser')
    book_list = soup.find()

def main():
    url = 'https://book.douban.com/top250'
    name_list = []
    while url:
        html = get_html(url)
        name, url = get_con(html)


if __name__ == '__main__':
    main()

