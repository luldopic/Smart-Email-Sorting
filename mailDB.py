# -*- coding: utf-8 -*-
"""
Communicate with Local SQL Server to sort emails

@author: Ludo
"""
import mysql.connector
import json


class emailDB:
    def __init__(self):
        self.connectDB()
        self.cursor = self.db.cursor()

    def connectDB(self):
        try:
            self.__connectToSQL__()
        except UnknownDatabase:
            self.__connectToSQL__(db_exist=False)
            self.cursor = self.db.cursor()
            self.cursor.execute("CREATE DATABASE GmailMail")

    def createTable(self, table_name, table_columns=None):
        if not self.checkTableExist(table_name):
            try:
                SQL = "CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY);".format(name=table_name)
                self.cursor.execute(SQL)
            except Exception as e:
                print(e)
        else:
            pass

    def checkTableExist(self, table_name):
        try:
            SQL = "SHOW TABLES LIKE '{name}'".format(name=table_name)
            self.cursor.execute(SQL)
            if self.cursor.arraysize != 0:
                print("Table exists")
                return True
            else: return False
        except Exception as e:
            print(e)

    def addTableColumn(self, table_name, table_column):
        SQL = """
            IF NOT EXISTS( 
                SELECT
                    column_name
                FROM
                    INFORMATION.SCHEMA.COLUMNS
                WHERE
                    TABLE_NAME = '{name}'
                    AND COLUMN_NAME = '{column_name}')
                ALTER TABLE {name} ADD ({column_name} {column_type});""".format(name=table_name, column_name=table_column[0], column_type = table_column[1])
        self.cursor.execute(SQL)

    def __connectToSQL__(self, db_exist=True):
        with open("MySQLcredentials.json") as handler:
            try:
                credentials = json.load(handler)
                if db_exist:
                    self.db = mysql.connector.connect(host=credentials["host"], user=credentials["user"],
                                                      password=credentials["password"], database="GmailMail")
                else:
                    self.db = mysql.connector.connect(host=credentials["host"], user=credentials["user"],
                                                      password=credentials["password"])
                print("Successful Connection")
            except Exception as e:
                error = str(e)
                if error.__contains__("Unknown database"):
                    raise UnknownDatabase("Database cannot be found")
                else:
                    print(e)
            finally:
                del credentials


class UnknownDatabase(Exception):
    pass

class UnknownTable(Exception):
    pass
