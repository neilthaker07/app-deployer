import mysql.connector
from flask import json
import collections
import DbConstants

class Project:
    project_id=None
    database=None
    user_name=None


    def __init__(self, user_name,project_id):
        self.user_name=user_name
        self.project_id=project_id
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    def ViewProjectSpecific(self):
      cursor = self.database.cursor()
      try:
        query = """SELECT * FROM project WHERE user_name=%s AND project_id=%s"""
        cursor.execute(query,(self.user_name,self.project_id))
        row = cursor.fetchone()
      #print 'view specific project of user'
      except mysql.connector.Error as err:
        cursor.close()
        self.database.close()
        return "err"
      objects_list = []
      # d = collections.OrderedDict()
      # d['project_name'] = row[1]
      # d['project_url'] = row[2]
      # objects_list.append(d)
      # j = json.dumps(objects_list)
      print row
      cursor.close()
      self.database.close()
      return row

    def DeleteProjectSpecific(self):
      cursor = self.database.cursor()
      try:
        query = """DELETE FROM project WHERE project_id=%s"""
        cursor.execute(query,(self.project_id,))
        self.database.commit()
      except mysql.connector.Error as err:
         cursor.close()
         self.database.close()
         return err
      cursor.close()
      self.database.close()
      return 'ok'
    
    # def get_project_details():

