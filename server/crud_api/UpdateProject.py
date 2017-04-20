import mysql.connector
from flask import json

class UpdateProject:
    project_id=None
    projectName = None
    projectURL = None
    database=None

    def __init__(self, requestJson, project_id):
        self.jsonObject=requestJson.get_json()
        self.projectName =self.jsonObject['projectName']
        self.projectURL = self.jsonObject['projectUrl']
        self.project_id=project_id
        self.database = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')

    def UpdateProjectSpecific(self):
      cursor = self.database.cursor()
      query = """UPDATE project SET project_name=%s,project_url=%s WHERE project_id=%s"""
      cursor.execute(query, (self.projectName, self.projectURL, self.project_id))
      self.database.commit()
      cursor.close()
      self.database.close()
      print 'update specific project of user'