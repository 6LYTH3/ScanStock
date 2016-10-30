#!/usr/bin/env python

from pymongo import MongoClient

def Connect():
    client = MongoClient('192.168.99.100', 27017)
    db = client['stockdb']
    return db

def Insert(db, stock):
    try:
        db.stocks.insert_one(stock)
    except Exception, e:
        print str(e)

def FindAll(db):
    try:
        return db.stocks.find()
    except Exception, e:
        print str(e)

