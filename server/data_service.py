import mysql.connector
from flask import json
import datetime
import collections
import DbConstants

class DataService:

    database=None
    def __init__(self):
        self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)

    def insertAgent(agent):
        cursor = self.database.cursor()
        try:
            query = """INSERT INTO agent (topic,agent_name,ip) VALUES (%s,%s,%s,%s)"""
            cursor.execute(query, (agent.topic,agent.agent_name, agent.ip))
            self.database.commit()
            result = self.get_agent_id()
            return result
        except mysql.connector.Error as err:
            cursor.close()
            self.database.close()
            return "err"

    def get_agent_id(id):
        cursor = self.database.cursor()
        query = """SELECT agent FROM agent WHERE id = %s"""
        cursor.execute(query, (id))
        row = cursor.fetchone()
        cursor.close()
        self.database.close()
        return row
