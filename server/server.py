from flask import Flask,abort,jsonify
from flask import request
import mysql.connector
from flask import json
import publisher
from Models import Deployment
import DbConstants
import datetime

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/git-updates", methods=['POST'])
def deploy_app():
    request_json=request.get_json() 

    repository=request_json['repository']
    git_url=repository['url']

    publisher.publish(git_url)
    return "sent-update"
#Rest_endpoint for inserting deployment status
@app.route("/v1/deployment",methods=['POST'])
def insert_deployer():
    if request.method=='POST':
        json_request_body=request.get_json()
        # print(json_request_body['agent_id'])
        # print(json_request_body['status'])
        deployer = Deployment(json_request_body['agent_id'],json_request_body['status'])
        result=deployer.Insert_deployer()
        print result
        return str(result),201

#rest_endpoit to update deployment status
@app.route("/v1/change_deploy_status",methods=['PUT'])
def deploy_status():
    if request.method=='PUT':
        json_request_body=request.get_json()
        print(json_request_body['id'])
        database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        cursor = database.cursor()
        try:
            query = """UPDATE deployment SET status=%s WHERE id=%s"""
            cursor.execute(query, (json_request_body['status'],json_request_body['id']))
            database.commit()
            return jsonify({'response': "Sucess"}),200
        except mysql.connector.Error as err:
            cursor.close()
            database.close()
            return jsonify({'response': "Error"}),500   

# @app.route("/v1/register/<topic>", methods=['POST'])
# def deploy_app():
#     request_json=request.get_json() 

#     agent_ip=request_json['agent_ip']
#     agent_name=request_json['agent_name'] 
#     return "sent-update"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3007)
