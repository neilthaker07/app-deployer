import mysql.connector
from flask import json
import datetime
import collections
import DbConstants

class DataService:

    database=None
    def __init__(self):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    def get_topic(self,url):
        database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                           database=DbConstants.DATABASE)
        cursor = database.cursor()
        query = """SELECT topic FROM project WHERE project_url= '""" + url + """'"""
        cursor.execute(query)
        output = cursor.fetchone()
        cursor.close()
        database.close()
        result = output[0]
        return result;


