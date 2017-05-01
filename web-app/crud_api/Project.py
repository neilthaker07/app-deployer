import mysql.connector
from flask import json
import collections

class Project:
    project_id=None
    database=None
    user_name=None

    def __init__(self, user_name,project_id):
        self.user_name=user_name
        self.project_id=project_id
        self.database = mysql.connector.connect(user='root', passwd='root', host='52.52.67.116', database='app_deployer_db')        

    def ViewProjectSpecific(self):
      cursor = self.database.cursor()
      try:
        query = """SELECT * FROM project WHERE user_name=%s AND project_id=%s"""
        cursor.execute(query,(self.project_id,self.user_name))
      #print 'view specific project of user'
      except mysql.connector.Error as err:
        cursor.close()
        self.database.close()
        return "err"
      row = cursor.fetchone()
      objects_list = []
      # d = collections.OrderedDict()
      # d['project_name'] = row[1]
      # d['project_url'] = row[2]
      # objects_list.append(d)
      # j = json.dumps(objects_list)
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
