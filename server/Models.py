import mysql.connector
from flask import json
import collections
import DbConstants


class Agent:
    id=None
    topic=None
    agent_name=None
    agent_ip=None

    def __init__(self, id, topic, agent_name, agent_ip):
        self.id=id;
        self.topic=topic;
        self.agent_name=agent_name;
        self.agent_ip=agent_ip;

class Deployment:
    agent_id=None
    status=None
    def __init__(self, agent_id,status):
        self.agent_id=agent_id
        self.status=status
        self.database=None
    
    def Insert_deployer(self):
         self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
         cursor = self.database.cursor()
         try:
            query = """INSERT INTO deployment (agent_id,status) VALUES (%s,%s)"""
            cursor.execute(query,(self.agent_id,self.status))
            self.database.commit()
            id = cursor.lastrowid;
            cursor.close()
            self.database.close()
            return id
         except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return "err"