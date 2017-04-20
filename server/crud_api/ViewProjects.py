import mysql.connector
from flask import json
import collections

class ViewProjects:
    username=None
    database=None

    def __init__(self, username):
        self.username=username
        self.database = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')        

    def ViewProjectsMethod(self):
      cursor = self.database.cursor()
      query = """SELECT * FROM project WHERE user_name=%s"""
      cursor.execute(query,(self.username,))
      print 'view all projects of user'
      rows = cursor.fetchall()
      objects_list = []
      for row in rows:
        d = collections.OrderedDict()
        d['project_name'] = row[1]
        d['project_url'] = row[2]
        objects_list.append(d)
      j = json.dumps(objects_list)
      cursor.close()
      self.database.close()
      return j