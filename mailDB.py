# -*- coding: utf-8 -*-
"""
Communicate with Local SQL Server to sort emails

@author: Ludo
"""
import mysql.connector
import json


class myDB:
    def __init__(self, database_name):
        self.createDB(database_name)

    def createDB(self, database_name):
        self.__connectToSQL__(database_name)
        if self.db_exists != True:
            cursor = self.db.cursor()
            cursor.execute("CREATE DATABASE %s", database_name)
        else:
            pass

    def createTable(self, table_name, table_columns):
        pass

    def __connectToSQL__(self, database_name):
        with open("MySQLcredentials.json") as handler:
            try:
                credentials = json.load(handler)
                self.db = mysql.connector.connect(host=credentials["host"], user=credentials["user"],
                                                  password=credentials["password"], database=database_name)
                del credentials
                print("Successful Connection")
            except Exception as e:
                error = str(e)
                if error.__contains__("Unknown Database"):
                    self.db_exists = False
                else:
                    print(e)


test = myDB("Gmail Mail")
