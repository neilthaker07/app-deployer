import mysql.connector
from flask import json
import datetime
import collections
import DbConstants

class DataServiceRest:

    database=None
    def __init__(self, project_id):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        self.project_id = project_id

    def get_agent_info(self):
        cursor = self.database.cursor()
        try:
            query = """Select A.AGENT_ID,A.TOPIC,A.AGENT_NAME,A.DEPLOYMENT_DATE,A.STATUS from (SELECT AGENT_NAME,AGENT_ID,DEPLOYMENT_DATE,TOPIC, deployment.STATUS FROM agent, deployment WHERE agent.id=deployment.agent_id AND agent.topic = (SELECT topic FROM project WHERE project_id=%s)) AS A INNER JOIN (select  agent_id  , max(deployment_date) AS DEPLOYMENT_DATE  from deployment d    group by agent_id) AS  B ON (A.AGENT_ID=B.AGENT_ID AND A.DEPLOYMENT_DATE=B.DEPLOYMENT_DATE)"""
            cursor.execute(query, (self.project_id,))
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
            d['deployment_date'] = row[3]
            d['status'] = row[4]
            objects_list.append(d)
        j = json.dumps(objects_list)
        print j
        cursor.close()
        self.database.close()
        return j
