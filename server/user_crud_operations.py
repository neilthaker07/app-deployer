from flask import Flask
from flask import request
from flask import json
import time

import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
	   	                 user="root",
	                   	passwd="root",
	                   	host="localhost",
	                   	db="app_deployer_db")

class ProcessData:
	projectId = None
	projectName = None
	projectURL = None
	topic = None
	db1_info = None

	def __init__(self, name, url, database):
		sel
		self.projectName = name
		self.project_URL = url
		self.topic = name+time.now()
		self.db1_info = database

	def insertData(self):
		cur = db.cursor()
		query = """INSERT INTO app_deployer_db.project (project_name,project_url,topic) VALUES (%s,%s,%s)"""
		cur.execute(query, (self.projectName, self.project_URL, self.topic))

	def updateData(self):
		cur = db.cursor()
		query = """UPDATE app_deployer_db.project SET project_name=%s,project_url=%s WHERE project_id=%s"""
		cur.execute(query, (self.projectName, self.project_URL, self.projectId))

	def deleteData(self):
		cur = db.cursor()
		query = """DELETE FROM app_deployer_db.project """
		cur.execute(query, (self.projectName, self.project_URL))

	def selectId(self):
		cur = db.cursor()
		query = """SELECT project_id FROM app_deployer_db.project WHERE project_name=%s """
		cur.execute(query, (self.projectName))		


@app.route("/v1/creation", methods=['POST', 'PUT'])
def userInput():
	if request.methods == 'POST':
		request_json=request.get_json()
		projectName=request_json['project_name']
		projectURL=request_json['project_url']
		processing = ProcessData(None, projectName, projectURL, db)
		processing.insertData()
	elif request.methods == 'PUT':
		ProcessData(projectId, projectName, projectURL, db)
		request_json=request.get_json()
		projectName=request_json['project_id']
		projectName=request_json['project_name']
		projectURL=request_json['project_url']
		processing = ProcessData(projectId, projectName, projectURL, db)
		processing.updateData()


@app.route("/v1/view")
def updateProjects():
	request_json=request.get_json()
	projectName=request_json['project_name']
	projectURL=request_json['project_url']
	processing = ProcessData(projectName, projectURL, db)
	processing.insertData()



db.commit()
db.close()

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
