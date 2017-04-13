import paho.mqtt.client as mqtt



def publish(git):
    client = mqtt.Client()
    client.connect("iot.eclipse.org", 1883, 60)
    client.publish("$SYS/broker/https://github.com/rashmishrm/sample-repo","update");
