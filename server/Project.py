import MySQLdb
from flask import json

class Project:
    username=None
    projectName = None
    projectURL = None
    topic = None
    database=None
    jsonObject=None

    def __init__(self,requestJson):
        self.jsonObject=requestJson.get_json()
        self.projectName =jsonObject['projectName']
        self.project_URL = jsonObject['projectUrl']
        self.username=jsonObject['userName']
        self.topic = projectName+time.clock()
        self.database = MySQLdb.connect(
	   	                 user="root",
	                   	passwd="root",
	                   	host="localhost",
	                   	db="app_deployer_db")
                           
		
    def InsertProject(self):
		cur = self.database.cursor()
		query = """INSERT INTO app_deployer_db.project (username,project_name,project_url,topic) VALUES (%s,%s,%s,%s)"""
		cur.execute(query, (self.username,self.projectName, self.project_URL, self.topic))

    def UpdateProject(self):
		cur = self.database.cursor()
		query = """UPDATE app_deployer_db.project SET project_name=%s,project_url=%s WHERE topic=%s AND user_name=%s"""
		cur.execute(query, (self.projectName, self.project_URL, self.topic,self.username))
    
    def DeleteProject(self):
		cur = self.database.cursor()
		query = """DELETE FROM app_deployer_db.project WHERE topic=%s AND user_name=%s"""
		cur.execute(query, (self.topic,self.username))

    def ViewProjects(self):
		cur = self.database.cursor()
		query = """SELECT * FROM app_deployer_db.project WHERE user_name=%s """
		cur.execute(query, (self.projectName))
        return self.convert_to_Json(cur)

    def convert_to_Json(self,cur):
        rows = cur.fetchall()
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['projectName'] = row.project_name
            d['projectUrl'] = row.project_url
            objects_list.append(d)
        
        j = json.dumps(objects_list)
        return j
    