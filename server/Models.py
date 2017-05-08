import mysql.connector
from flask import json
import collections
import DbConstants
import datetime

class Agent:
    id=None
    topic=None
    agent_name=None
    ip=None

    def __init__(self, id,topic,agent_name,ip):
        self.id=id
        self.topic=topic
        self.agent_name=agent_name
        self.ip=ip

class Deployment:
    agent_id=None
    status=None
    def __init__(self, agent_id,status):
        self.agent_id=agent_id
        self.status=status
        self.deployment_date=datetime.datetime.now()
    
    def Insert_deployer(self):
         database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
         cursor = database.cursor()
         try:
            query = """INSERT INTO deployement (agent_id,status,deployment_date) VALUES (%s,%s,%s)"""
            cursor.execute(query, (self.agent_id,self.status,self.deployment_date))
            database.commit()
            query2 = """SELECT id FROM deployment WHERE agent_id=%s"""
            cursor.execute(query,(self.agent_id))
            row = cursor.fetchone()
            return row
         except mysql.connector.Error as err:
            cursor.close()
            database.close()
            return "err"






