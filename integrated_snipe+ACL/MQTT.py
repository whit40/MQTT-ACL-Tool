# MQTT functions go here (publish, subscribe, etc.)
import sys
import paho.mqtt.client as paho


successfultopics = set([])


def create_client(username, password):
    print("Creating client")
    client = paho.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username, password)

    return client


def client_connect(client, host, port):
    print("Connecting to host")
    client.connect(host, port)


def on_message(client, userdata, msg):
    print("Topic: ", msg.topic, " Message: ", str(msg.payload))
    successfultopics.add(msg.topic)
    print("List of successful topics is now: ", successfultopics)


def on_connect(client, userdata, flags, rc):
    global connected
    if rc == 0:
        print("Successfully connected")
    else:
        print("Authorization error, wrong password")
        sys.exit(2)