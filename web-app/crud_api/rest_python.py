from flask import Flask
from flask import request,render_template,send_file,send_from_directory
from flask import json
from UserInfo import UserInfo
from Projects import Projects
from Project import Project
from ViewProjects import ViewProjects
from UpdateProject import UpdateProject

app = Flask(__name__)

@app.route("/v1/userSignup",methods=['POST'])
def userSignup():
	if request.method == 'POST':
		user = UserInfo(request)
		return user.insertUser()
		#return "HEEEEHHAAAA SIGNUP"

@app.route("/v1/userLogin",methods=['POST'])
def userLogin():
	if request.method == 'POST':
		user = UserInfo(request)
		return user.loginUser()
		#return "HEEEEHHAAAA LOGIN"

@app.route("/v1/<user_name>/projects",methods=['POST','GET'])
def createAndViewProjects(user_name):
	if request.method == 'POST':
		projects = Projects(request, user_name)
		projects.InsertProject()
		return "HEEEEHHAAAA PROJECT CREATION"
	elif request.method == 'GET':
		viewProjects = ViewProjects(user_name)
		return viewProjects.ViewProjectsMethod()
		#return "HEEEEHHAAAA PROJECTS VIEW"

# Dependent on UI
@app.route("/v1/<user_name>/projects/<project_id>",methods=['PUT','GET','DELETE'])
def viewUpdateDeleteProject(user_name, project_id):
	if request.method == 'GET':
		project = Project(project_id)
		return project.ViewProjectSpecific()
		#return "HEEEEHHAAAA PROJECT VIEW SPECIFIC"
	elif request.method == 'DELETE':
		project = Project(project_id)
		project.DeleteProjectSpecific()
		return "HEEEEHHAAAA PROJECT DELETE SPECIFIC"
	elif request.method == 'PUT':
		updateProject = UpdateProject(request, project_id)
		updateProject.UpdateProjectSpecific()
		return "HEEEEHHAAAA PROJECT UPDATE SPECIFIC"

@app.route("/")
def index():
   return send_file("index.html")

@app.route("/ui/<path:path>")
def file(path):
   return send_from_directory("ui",path)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=3005)
