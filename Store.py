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

def ConvertToIntBy(str):
    i = re.sub(',','',str.string.strip())
    return float(i)


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
            "Assets": ConvertToIntBy(fin[1]),
            "Liabilities": ConvertToIntBy(fin[2]), 
            "Equity": ConvertToIntBy(fin[3]),
            "Paid-up Capital": ConvertToIntBy(fin[4]),
            "Revenue": ConvertToIntBy(fin[5]),
            "Net Profit": ConvertToIntBy(fin[6]),
            "EPS": ConvertToIntBy(fin[7]),
            "ROA": ConvertToIntBy(fin[9]),
            "ROE": ConvertToIntBy(fin[10]),
            "Margin": ConvertToIntBy(fin[11]),
            "Last Price": ConvertToIntBy(fin[12]),
            "Market Cap": ConvertToIntBy(fin[13]),
            "PE": ConvertToIntBy(fin[15]),
            "PBV": ConvertToIntBy(fin[16]),
            "Book Value": ConvertToIntBy(fin[17]),
            "Yield": ConvertToIntBy(fin[18])}
    db = MongoCli.Connect()
    MongoCli.Insert(db, stock)

if __name__ == '__main__':
    Symbol = 'JAS'
    Store()
