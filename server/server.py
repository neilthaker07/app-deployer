from flask import Flask
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
@app.route("/v1/deployment/<agent_id,status>",Method=['POST'])
def insert_deployer(agent_id,status):
    if request.method=='POST':
        deployer = Deployment(agent_id,status)
        return deployer.Insert_deployer()

#rest_endpoit to update deployment status
@app.route("/v1/change_deploy_status/<id,status>",Method=['PUT'])
def deploy_status(id,status):
    if request.method=='PUT':
        database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
        cursor = database.cursor()
        try:
            query = """UPDATE deployment SET status=%s,deployment_date=datetime.datetime.now() WHERE id=id"""
            cursor.execute(query, (status))
            database.commit()
            return "Ok"
        except mysql.connector.Error as err:
            cursor.close()
            database.close()
            return "Err"   

@app.route("/v1/register/<topic>", methods=['POST'])
def deploy_app():
    request_json=request.get_json() 

    agent_ip=request_json['agent_ip']
    agent_name=request_json['agent_name'] 
    return "sent-update"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3007)
