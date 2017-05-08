from flask import Flask,abort,jsonify,Response,json
from flask import request
from flask import request,render_template,send_file,send_from_directory
from UserInfo import UserInfo
from Projects import Projects
from Project import Project
from ViewProjects import ViewProjects
from UpdateProject import UpdateProject
import mysql.connector
import DbConstants


app = Flask(__name__)
# Create a new user, if user already exists then return the response to select another user name else, return user id
@app.route("/v1/userSignup",methods=['POST'])
def userSignup():
	if request.method == 'POST':
		user = UserInfo(request)
		result = user.insertUser()
		if(result == '201'):
			user_id = user.get_user_id()
			return jsonify({'response': user_id}), 201
		return result, 400 #here the result is not json , not sure how to return the response here (should it be json?)


@app.route("/v1/getTopic",methods=["POST"])
def get_topic():
	request_json = request.get_json();
	url = request_json['git_url'];
	print url
	database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
									   database=DbConstants.DATABASE)
	cursor = database.cursor()
	query = """SELECT topic FROM project WHERE project_url= '"""+url+"'"
	print query
	cursor.execute(query)
	output = cursor.fetchone()
	print output
	result = output[0]
	print result
	return Response(result, status=200)




@app.route("/v1/userLogin",methods=['POST'])
def userLogin():
	if request.method == 'POST':
		user = UserInfo(request)
		result=user.loginUser()
		if(result == 'fail'):
			return jsonify({'user':'Not able to connect to db'}), 500 #(is this right?)
		elif(result =="true"):
			return jsonify({'response':'ok'})
		else:
			return jsonify({'response':'user name or password incorrect'}), 401

#never give 404??
#This return project_id to the user
@app.route('/v1/<user_name>/projects',methods=['POST','GET'])
def createAndViewProjects(user_name):
	if request.method == 'POST':
		print user_name
		projects = Projects(request, user_name)
		result=projects.InsertProject()
		return jsonify({'response':result})
	elif request.method == 'GET':
		viewProjects = ViewProjects(user_name)
		project_return = viewProjects.ViewProjectsMethod()
		if len(project_return)!=0:
			return project_return
		else:
			return jsonify({'response': 'No result Found'}),404


# Dependent on UI
@app.route("/v1/<user_name>/projects/<project_id>",methods=['PUT','GET','DELETE'])
def viewUpdateDeleteProject(user_name,project_id):
	if request.method == 'GET':
		project = Project(user_name,project_id)
		result =project.ViewProjectSpecific()
		if(result=="err"):
			return jsonify({'response':result}),500
		else:
			return jsonify({'response':result})
	elif request.method == 'DELETE':
		project = Project(user_name,project_id)
		result=project.DeleteProjectSpecific()
		if(result=="ok"):
			return jsonify({'response': result})
		else:
			return jsonify({'response':'try again'}),500 #is this true?
	elif request.method == 'PUT':
		updateProject = UpdateProject(user_name,request, project_id)
		result=updateProject.UpdateProjectSpecific()
		if(result == 'ok'):
			return jsonify({'response': result})
		return jsonify({'response': "error"}),500

# @app.route("/v1/<user_name>/projects/<project_url>")
# def get_project_details(usr_name,project_url):
# 	project = Project(user_name,project_url)
# 	result = project.get_project_details()



@app.route("/")
def index():
   return send_file("index.html")

@app.route("/ui/<path:path>")
def file(path):
   return send_from_directory("ui",path)


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=3005)
