import mysql.connector
from flask import json
import time
import collections
import DbConstants

class Projects:
    username=None
    projectName = None
    projectURL = None
    topic = None
    database=None
    jsonObject=None

    def __init__(self, requestJson, username):
        self.jsonObject=requestJson.get_json()
        self.projectName =self.jsonObject['projectName']
        self.project_URL = self.jsonObject['projectUrl']
        self.username=username
        print self.username
        self.topic = self.projectName + str(int(round(time.time() * 1000)))
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    # insert new project
    def InsertProject(self):
        cursor = self.database.cursor()
        try:
            query = """INSERT INTO project (user_name,project_name,project_url,topic) VALUES (%s,%s,%s,%s)"""
            cursor.execute(query, (self.username,self.projectName, self.project_URL, self.topic))
            self.database.commit()
            result = self.get_project_id(cursor)
            cursor.close()
            self.database.close()
            return result
        except mysql.connector.Error as err:
            print "err"
            cursor.close()
            self.database.close()
            return "err"

    def get_project_id(self,cursor):
        # self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        # cursor = self.database.cursor()
        print "in project_id"
        query = """SELECT project_id FROM project WHERE user_name = %s AND project_url=%s"""
        cursor.execute(query, (self.username,self.project_URL))
        row = cursor.fetchone()
        cursor.close()
        self.database.close()
        return row
