import mysql.connector
from flask import json
import collections
import DbConstants

class ViewProjects:
    username=None
    database=None

    def __init__(self, username):
        self.username=username
        #self.database = mysql.connector.connect(user='root', passwd='root', host='localhost', database='app_deployer_db')        

    def ViewProjectsMethod(self):
      cnx=mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE) 
      cursor = cnx.cursor()
      try:
        query = """SELECT * FROM project WHERE user_name=%s"""
        cursor.execute(query,(self.username,))
        print 'view all projects of user'
        rows = cursor.fetchall()
      except mysql.connector.Error as err:
        cursor.close()
        cnx.close()
        return err
      objects_list = []
      for row in rows:
        d = collections.OrderedDict()
        d['project_id'] = row[0]
        d['project_name'] = row[1]
        d['project_url'] = row[2]
        objects_list.append(d)
      j = json.dumps(objects_list)
      print j
      cursor.close()
      cnx.close()
      return j