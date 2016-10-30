#!/usr/bin/env python

import MongoCli

def Great():
    db = MongoCli.Connect()
    for stock in MongoCli.FindAll(db):
        if (stock['Equity'] > stock['Liabilities']) and (stock['ROE'] > 20):
            print "Stock: {0:5} List Price: {1}".format(stock['Symbol'], stock['Last Price'])
    
if __name__ == '__main__':
    Great()
