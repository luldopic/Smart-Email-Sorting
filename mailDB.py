# -*- coding: utf-8 -*-
"""
Communicate with Local SQL Server to sort emails

@author: Ludo
"""
import mysql.connector
import json

class database:
    def __init__(self):
        get

    def getDBName(self):
        with open("MySQLcredentials.json") as handler:
            try:
                credentials = json.load(handler)
                self.db_name = credentials["database"]
            except Exception as e:
                print(e)
                
    def connectToSQL():
        with open("MySQLcredentials.json") as handler:
            try:
                credentials = json.load(handler)
                db = mysql.connector.connect(host=credentials["host"],user=credentials["user"],password = credentials["password"])
                self.db_name = credentials[db]
                del(credentials)
            except Exception as e:
                pass

test = connectToSQL()