import paho.mqtt.client as mqtt
import subprocess
import shlex
import os
import requests

TOPIC='https://github.com/rashmishrm/sample-repo'
SERVER = "0.0.0.0:3007"
DISCOVER_AGENT_URL ="http://"+SERVER+"/v1/register/"+TOPIC
DEPLOY_AGENT_URL_ ="http://"+SERVER+"/v1/deploy/"
DEPLOY_AGENT_URL_UPDATE = "http://"+SERVER+"/v1/deploy/"
agent_id = None
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
    os.system('sh agent_deployer.sh '+TOPIC)
    update()


def register():
    url = DISCOVER_AGENT_URL
    request =  '{
    "agent_name":"abc",
    "agent_ip":"ip"
    }'
    response = requests.post(url, data=request)
    agent_id = response["agent_id"]


def deploy():
    url = DEPLOY_AGENT_URL
    request =  '{
    "agent_id":agent_id,
    "status":"deploying"
    }'
    response = requests.post(url, data=request)
    deployment_id = response["deployment_id"]

def update():
    url = DEPLOY_AGENT_URL
    request =  '{
    "deployment_id":deployment_id,
    "status":"deployed"
    }'
    response = requests.post(url, data=request)


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
