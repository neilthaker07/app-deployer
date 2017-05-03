import mysql.connector
from flask import json
import DbConstants

class UpdateProject:
    user_name=None
    project_id=None
    projectName = None
    projectURL = None
    database=None

    def __init__(self,user_name,requestJson,project_id):
        self.user_name=user_name
        self.jsonObject=requestJson.get_json()
        self.projectName =self.jsonObject['projectName']
        self.projectURL = self.jsonObject['projectUrl']
        self.project_id=project_id
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    def UpdateProjectSpecific(self):
        cursor = self.database.cursor()
        try:
            query = """UPDATE project SET project_name=%s,project_url=%s WHERE user_name=%s AND project_id=%s"""
            cursor.execute(query, (self.projectName, self.projectURL,self.user_name, self.project_id))
            self.database.commit()
            result='ok'
        except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return "err"
        cursor.close()
        self.database.close()
        return result
      