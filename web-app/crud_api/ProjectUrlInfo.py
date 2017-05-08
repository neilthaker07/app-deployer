import mysql.connector
from flask import json, jsonify
import Constants
import requests

class ProjectUrlInfo:
    url=None

    def __init__(self,requestJson):
        jsonObject=requestJson.get_json()
        self.url = jsonObject['url']

    #signup
    def triggerDeployment(self):
        url = Constants.DEPLOYER_SERVICE_URL
        data={"repository":{"url":self.url}}
        response = requests.post(url, json=data)
        return response
