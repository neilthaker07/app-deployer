from flask import Flask
from flask import request

from flask import json
import publisher
from Models import Agent
from data_service import DataService

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/git-updates", methods=['POST'])
def deploy_app():
    request_json=request.get_json() ;
    repository=request_json['repository'];
    git_url=repository['url'];

    publisher.publish(git_url);
    return "sent-update"

@app.route("/v1/register/<topic>", methods=['POST'])
def agent_deployment(topic):
    request_json=request.get_json() ;

    agent_ip=request_json['agent_ip'];
    agent_name=request_json['agent_name'];

    agent = Agent("", topic, agent_name, agent_ip)

    dataService = DataService(agent, "", "")
    return dataService.insertAgent()
    #return "sent-update"

@app.route("/v1/getTopic/<id>", methods=['GET'])
def list_of_agents_deployment(id): #agents
    agent = Agent(id, "","","")
    dataService = DataService(agent,"",agent.id)
    return dataService.get_agent_id()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3007)
