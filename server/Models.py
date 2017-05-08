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
    id=None
    agent_id=None
    deployment_date=None
    status=None

    def __init__(id, agent_id,deployment_date,status):
        self.id=id;
        self.agent_id=agent_id;
        self.deployment_date=deployment_date;
        self.status=status;
