#!/usr/bin/env python

# The Finance.py
# - Get Financial data all shared from Set.or.th
# - Store some reponse data | Assets, Liabilities, Equity, ROA, ROE,
#   per shared

import re
import requests
from bs4 import BeautifulSoup
import MongoCli

Symbol = 'PTT'

def GetData():
    url = 'http://www.set.or.th/set/companyhighlight.do?symbol=' + Symbol + '&ssoPageId=5&language=en&country=US'
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    return r.text

def GrepTag():
    # html_doc = GetData()
    # soup = BeautifulSoup(html_doc, "html.parser")
    soup = BeautifulSoup(open("raw.html"), "html.parser")
    td = soup.find_all("td", style="background-color: #EAF0FE;")
    return td

def PrintData():
    fin = GrepTag()
    print '{0}'.format(Symbol)
    print 'Assets           {0}'.format(fin[1].string.strip())
    print 'Liabilities      {0}'.format(fin[2].string.strip())
    print 'Equity           {0}'.format(fin[3].string.strip())
    print 'Paid-up Capital  {0}'.format(fin[4].string.strip())
    print 'ROE(%)           {0}'.format(fin[10].string.strip())
    print 'Last Price(Bath) {0}'.format(fin[12].string.strip())

def Store():
    fin = GrepTag()
    stock = {"Symbol": Symbol, 
            "Assets": fin[1].string.strip(),
            "Liabilities": fin[2].string.strip(), 
            "Equity": fin[3].string.strip(),
            "Paid-up Capital": fin[4].string.strip(),
            "Revenue": fin[5].string.strip(),
            "Net Profit": fin[6].string.strip(),
            "EPS": fin[7].string.strip(),
            "ROA": fin[9].string.strip(),
            "ROE": fin[10].string.strip(),
            "Margin": fin[11].string.strip(),
            "Last Price": fin[12].string.strip(),
            "Market Cap": fin[13].string.strip(),
            "PE": fin[15].string.strip(),
            "PBV": fin[16].string.strip(),
            "Book Value": fin[17].string.strip(),
            "Yield": fin[18].string.strip()}
    db = MongoCli.Connect()
    MongoCli.Insert(db, stock)

if __name__ == '__main__':
    Symbol = 'JAS'
    Store()
