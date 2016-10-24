#!/usr/bin/env python

# The Finance.py
# - Get Financial data all shared from Set.or.th
# - Store some reponse data | Assets, Liabilities, Equity, ROA, ROE,
#   per shared

import re
import requests
from bs4 import BeautifulSoup

Symbol = 'PTT'

def GetData():
    url = 'http://www.set.or.th/set/companyhighlight.do?symbol=' + Symbol + '&ssoPageId=5&language=en&country=US'
    headers = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    return r.text

def GetUnitFromTdTag(td):
    line = re.sub(r'<\S+', '', str(td))                              # Remove <td> </td> tag
    u = re.sub(r'style="background-color: #EAF0FE;">','', line)   # Remove Style
    return u.strip()

def GrepTag():
    html_doc = GetData()
    soup = BeautifulSoup(html_doc, "html.parser")
    td = soup.find_all("td", style="background-color: #EAF0FE;")
    return td

def PrintData():
    fin = GrepTag()
    print '{0}'.format(Symbol)
    print 'Assets           {0}'.format(GetUnitFromTdTag(fin[1]))
    print 'Liabilities      {0}'.format(GetUnitFromTdTag(fin[2]))
    print 'Equity           {0}'.format(GetUnitFromTdTag(fin[3]))
    print 'Paid-up Capital  {0}'.format(GetUnitFromTdTag(fin[4]))
    print 'ROE(%)           {0}'.format(GetUnitFromTdTag(fin[10]))
    print 'Last Price(Bath) {0}'.format(GetUnitFromTdTag(fin[12]))

if __name__ == '__main__':
    Symbol = 'CHO'
    PrintData()
