import mysql.connector
from flask import json
import collections

class Project:
    project_id=None
    database=None

    def __init__(self, project_id):
        self.project_id=project_id
        self.database = mysql.connector.connect(user='root', passwd='root', host='52.52.67.116', database='app_deployer_db')        

    def ViewProjectSpecific(self):
      cursor = self.database.cursor()
      query = """SELECT * FROM project WHERE project_id=%s"""
      cursor.execute(query,(self.project_id,))
      print 'view specific project of user'
      row = cursor.fetchone()
      objects_list = []
      d = collections.OrderedDict()
      d['project_name'] = row[1]
      d['project_url'] = row[2]
      objects_list.append(d)
      j = json.dumps(objects_list)
      cursor.close()
      self.database.close()
      return j

    def DeleteProjectSpecific(self):
      cursor = self.database.cursor()
      query = """DELETE FROM project WHERE project_id=%s"""
      cursor.execute(query,(self.project_id,))
      self.database.commit()
      cursor.close()
      self.database.close()
      print 'delete specific project of user'
