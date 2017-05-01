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
        cnx = mysql.connector.connect(user='root', passwd='root', host='52.52.67.116', database='app_deployer_db')
        cursor = cnx.cursor()
        query = """SELECT * FROM user WHERE user_name = %s"""
        cursor.execute(query, (self.username,))
        row = cursor.fetchone()
        if row is not None:
            print 'pls select another name'
            return 'pls select another name'
        else:
<<<<<<< Updated upstream:web-app/crud_api/UserInfo.py
            insertQuery = """INSERT INTO user (user_name, user_pass) VALUES (%s,%s)"""
            cursor.execute(insertQuery, (self.username, self.password))
            cnx.commit()
            cursor.close()
            cnx.close()
            return 'user created'

=======
            try:
                insertQuery = """INSERT INTO user (user_name, user_pass) VALUES (%s,%s)"""
                cursor.execute(insertQuery, (self.username, self.password))
                cnx.commit()
            except mysql.connector.Error as err:
                cursor.close()
                cnx.close()
                return err
        return '201'
>>>>>>> Stashed changes:server/crud_api/UserInfo.py
    #login
    def loginUser(self):
        cnx = mysql.connector.connect(user='root', passwd='root', host='52.52.67.116', database='app_deployer_db')
        cursor = cnx.cursor()
        try:
            query = """SELECT * FROM user WHERE user_name = %s AND user_pass=%s"""
            cursor.execute(query, (self.username, self.password))
            row = cursor.fetchone()
            cnx.commit()
        except mysql.connector.Error as err:
            cursor.close()
            cnx.close()
            return 'fail'
        if row is not None:
            print 'success login'
            result = 'true'
        else:
            print 'fail login'
            result = 'false'
        cnx.commit()
        cursor.close()
        cnx.close()
<<<<<<< Updated upstream:web-app/crud_api/UserInfo.py
        return self.username
=======
        return result


    def get_user_id(self):
        cnx = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')
        cursor = cnx.cursor()
        query = """SELECT user_name FROM user WHERE user_name = %s AND user_pass=%s"""
        cursor.execute(query, (self.username, self.password))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return row
>>>>>>> Stashed changes:server/crud_api/UserInfo.py
