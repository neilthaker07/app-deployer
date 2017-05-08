import mysql.connector
from flask import json
import datetime
import collections
import DbConstants

class DataService:

    database=None
    def __init__(self, agent, ip, agent_id):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        self.agent = agent
        self.ip = self.agent.agent_ip
        self.agent_id = agent_id

    def insertAgent(self):
        cursor = self.database.cursor()
        try:
            query = """INSERT INTO agent (topic,agent_name,ip) VALUES (%s,%s,%s)"""
            print self.agent.topic +"  "+self.agent.agent_name+ " "+ self.agent.agent_ip
            cursor.execute(query, (self.agent.topic, self.agent.agent_name, self.agent.agent_ip))
            self.database.commit()
            result = cursor.lastrowid
            return str(result)
        except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return "err"

    def get_agent_id(self):
        cursor = self.database.cursor()
        try:
            query = """SELECT * FROM agent, deployment WHERE agent.id=deployment.agent_id AND agent.id = %s"""
            cursor.execute(query, (self.agent_id,))
            rows = cursor.fetchall()
        except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return "err"
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['id'] = row[0] # its agent id
            d['topic'] = row[1]
            d['agent_name'] = row[2]
            d['ip'] = row[3]
            d['deployment_date'] = row[6]
            d['status'] = row[7]
            objects_list.append(d)
        j = json.dumps(objects_list)
        print j
        cursor.close()
        self.database.close()
        return j
