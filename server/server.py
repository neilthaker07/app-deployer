from flask import Flask,abort,jsonify
from flask import Flask, jsonify
from flask import request
import mysql.connector
from flask import json
import publisher
from Models import Deployment
import DbConstants
import datetime
import requests
from Models import Agent
from data_service import DataService

git_repo=''


app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"


def getTopic(gitUrl):
    ds = DataService();
    result = ds.get_topic(gitUrl);
    print '**********'
    print result
    return result


@app.route("/v1/git-updates", methods=['POST'])
def deploy_app():
    request_json=request.get_json()
    repository=request_json['repository']
    git_url=repository['url']
    topic = getTopic(git_url)
    publisher.publish(topic)
    return "sent-update"




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3007)
