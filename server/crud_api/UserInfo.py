import mysql.connector
from flask import json

class UserInfo:
    username=None
    password=None
    database=None
    jsonObject=None
    
    def __init__(self,requestJson):
        jsonObject=requestJson.get_json()
        self.username = jsonObject['username']
        self.password =  jsonObject['password']
    
    #signup
    def insertUser(self):
        cnx = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')
        cursor = cnx.cursor()
        query = """SELECT * FROM user WHERE user_name = %s"""
        cursor.execute(query, (self.username,))
        row = cursor.fetchone()
        if row is not None:
            print 'pls select another name'
            return 'pls select another name'
        else:
            insertQuery = """INSERT INTO user (user_name, user_pass) VALUES (%s,%s)"""
            cursor.execute(insertQuery, (self.username, self.password))
            cnx.commit()
            cursor.close()
            cnx.close()
            return 'user created'

    #login
    def loginUser(self):
        cnx = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')
        cursor = cnx.cursor()
        query = """SELECT * FROM user WHERE user_name = %s AND user_pass=%s"""
        cursor.execute(query, (self.username, self.password))
        row = cursor.fetchone()
        if row is not None:
            print 'success login'
        else:
            print 'fail login'
        cnx.commit()
        cursor.close()
        cnx.close()
        return self.username