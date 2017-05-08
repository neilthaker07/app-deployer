import mysql.connector
from flask import json
import datetime
import collections
import DbConstants

class DataServiceRest:

    database=None
    def __init__(self, agent_id):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        self.agent_id = agent_id

    def get_agent_info(self):
        cursor = self.database.cursor()
        try:
            query = """SELECT * FROM agent, deployment WHERE agent.id=deployment.agent_id AND agent.topic = (SELECT topic FROM project WHERE project_id=%s)"""
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
