import mysql.connector
from flask import json
import datetime
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
        self.topic = self.projectName + str(datetime.datetime.now())
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    # insert new project
    def InsertProject(self):
        cursor = self.database.cursor()
        try:
            query = """INSERT INTO project (user_name,project_name,project_url,topic) VALUES (%s,%s,%s,%s)"""
            cursor.execute(query, (self.username,self.projectName, self.project_URL, self.topic))
            self.database.commit()
            result = self.get_project_id()
            return result
        except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return err
    def get_project_id(self):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)  
        cursor = self.database.cursor()
        query = """SELECT project_id FROM project WHERE user_name = %s AND project_URL=%s"""
        cursor.execute(query, (self.username,self.project_URL))
        row = cursor.fetchone()
        cursor.close()
        self.database.close()
        return row