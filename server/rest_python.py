from flask import Flask
from flask import request
from flask import json
from Project import Project
import time
import MySQLdb
from UserInfo import UserInfo


app = Flask(__name__)

# db = MySQLdb.connect(
# 	   	                 user="root",
# 	                   	passwd="root",
# 	                   	host="localhost",
# 	                   	db="app_deployer_db")

	
# User log in information
@app.route("/v1/userSignUp",methods=['POST'])
def userSignUp():
	if request.method == 'POST':
		user = UserInfo(request)
		user.insertUser()

@app.route("/v1/userlogin",methods=['POST'])
def userlogin():
	if request.method == 'POST':
		user = UserInfo(request)
		user.validateUser(request)		
		

@app.route("/v1/userlogin/addProject", methods=['POST','GET'])
def userInput():
	project =  Project(request)
	if request.method == 'POST':
		project.InsertProject()
	else:
		return project.ViewProjects()

@app.route("/v1/userlogin/UpdateProject", methods=['PUT'])
def update():
	project =  Project(request)
	if request.method == 'PUT':
		project.UpdateProject()	
@app.route("/v1/userlogin/DeleteProject", methods=['DELETE'])
def delete():
	project =  Project(request)
	if request.method == 'DELETE':
		project.DeleteProject()
		

		


# @app.route("/v1/view")
# def updateProjects():
# 	request_json=request.get_json()
# 	projectName=request_json['project_name']
# 	projectURL=request_json['project_url']
# 	processing = ProcessData(projectName, projectURL, db)
# 	processing.insertData()





if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
