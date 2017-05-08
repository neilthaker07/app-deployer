import paho.mqtt.client as mqtt
import subprocess
import shlex
import os
import requests

TOPIC='mytopic'
GIT_URL="https://github.com/rashmishrm/sample-repo"
SERVER = "0.0.0.0:3005"
DISCOVER_AGENT_URL ="http://"+SERVER+"/v1/register/"+TOPIC
DEPLOY_AGENT_URL ="http://"+SERVER+"/v1/deployment"
DEPLOY_AGENT_URL_UPDATE = "http://"+SERVER+"/v1/change_deploy_status"
agent_id = 1
deployment_id =None


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/broker/"+TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    deploy()
    os.system('sh agent_deployer.sh '+GIT_URL)
    update()


def register():
    global agent_id
    url = DISCOVER_AGENT_URL
    request =  {
    "agent_name":"abc",
    "agent_ip":"ip"
    }
    response = requests.post(url, json=request)
    agent_id = response.text


def deploy():
    global agent_id
    global deployment_id
    print "deploying....."+agent_id
    url = DEPLOY_AGENT_URL
    request =  {
    "agent_id":agent_id,
    "status":"deploying"
    }
    response = requests.post(url, json=request)
    deployment_id = response.text


def update():
    global deployment_id
    print "deployed updating....."+deployment_id
    url = DEPLOY_AGENT_URL_UPDATE
    request =  {
    "id":deployment_id,
    "status":"deployed"
    }
    requests.put(url, json=request)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

#Registering agent on server
register()



# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
