import MySQLdb
from flask import json


class UserInfo:
    username=None
    password=None
    database=None
    jsonObject=None
    def __init__(self,requestJson):
        self.database = MySQLdb.connect(
	   	                 user="root",
	                   	passwd="root",
	                   	host="localhost",
	                   	db="app_deployer_db")
        jsonObject=requestJson.get_json()
        self.username = jsonObject['username']
        self.password =  jsonObject['password']
        #self.database = db
    
    def insertUser(self):
        cur = self.database.cursor()
        if self.validateUser:
            print "this is true"   
        else:  
            query = """INSERT INTO app_deployer_db.user (user_name,user_pass) VALUES (%s,%s)"""
            cur.execute(query,(self.username, self.password))
        

        
    def validateUser(self):
        cur = self.database.cursor()
        query="""SELECT COUNT(user_name) FROM app_deployer_db.user WHERE user_name = %s"""
        cur.execute(query,(self.username,))
        data=cur.fetchone()
        if data[0]==1:
            print "this is true" 
            return "true"  
        else:  
            print "false"
            return "false"


self.database.commit()
self.database.close()
     




 

 

