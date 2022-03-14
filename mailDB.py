# -*- coding: utf-8 -*-
"""
Communicate with Local SQL Server and Database

@author: Ludo
"""
import mysql.connector
import json


class emailDB:
    def __init__(self):
        self.connectDB()

    def connectDB(self):
        try:
            self.__connectToSQL__()
        except UnknownDatabase:
            self.__connectToSQL__(db_exist=False)
            SQL = "CREATE DATABASE GmailMail"
            self.executeSQLCursor(SQL)

    def createTable(self, table_name, table_columns=None):
        try:
            self.__checkTableExist__(table_name)
        except UnknownTable:
            SQL = "CREATE TABLE {name} (id INT AUTO_INCREMENT PRIMARY KEY);".format(name=table_name)
            self.executeSQLCursor(SQL)
        except TableAlreadyCreated:
            pass
        except Exception as e:
            print(e)

    def showALLTable(self):
        try:
            SQL = "SHOW TABLES"
            self.executeSQLCursor(SQL)
        except Exception as e:
            print(e)

    def addTableColumn(self, table_name, table_column):
        try:
            self.__checkColumnExist__(table_name, table_column[0])
        except UnknownColumn:
            SQL = "ALTER TABLE {name} ADD ({column_name} {column_type})".format(name=table_name,
                                                                                column_name=table_column[0],
                                                                                column_type=table_column[1])
            self.executeSQLCursor(SQL)
        except ColumnAlreadyCreated:
            pass

    """
    Insert a new record into table such that columns don't have to be hard-coded.
    As long as the entry is dictionary entry
    """
    def addEntry(self, table_name, entry):
        columns = str(tuple(entry.keys())).replace("'", "")
        values = str(tuple(entry.values()))
        SQL = "INSERT INTO {table} {columns} VALUES {values}".format(table=table_name, columns=columns, values=values)
        self.executeSQLCursor(SQL)
        self.db.commit()

    def retrieveEntry(self, table_name, column_names=None):
        if column_names is not None:
            columns = str(column_names).replace("'", "")  # column: tuple
            SQL = "SELECT {columns} FROM {table}".format(columns=columns, table=table_name)
        else:
            SQL = "SELECT * FROM {table}".format(table=table_name)
        res = self.executeSQLCursor(SQL)
        return res

    def executeSQLCursor(self, command):
        cursor = self.db.cursor()
        cursor.reset()
        cursor.execute(command)
        res = cursor.fetchall()
        cursor.close()
        return res

    def __checkTableExist__(self, table_name):
        SQL = "SHOW TABLES LIKE '{name}'".format(name=table_name)
        res = self.executeSQLCursor(SQL)
        if len(res) == 0:
            raise UnknownTable("Table cannot be found")
        else:
            raise TableAlreadyCreated("Table already created")

    def __checkColumnExist__(self, table_name, column_name):
        SQL = "SHOW COLUMNS FROM {table} LIKE '{column}'".format(table=table_name, column=column_name)
        res = self.executeSQLCursor(SQL)
        if len(res) == 0:
            raise UnknownColumn("Column cannot be found")
        else:
            raise ColumnAlreadyCreated("Column already created")

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


"""
List of specific Errors 
"""

class UnknownDatabase(Exception):
    pass

class UnknownTable(Exception):
    pass

class TableAlreadyCreated(Exception):
    pass

class UnknownColumn(Exception):
    pass

class ColumnAlreadyCreated(Exception):
    pass
