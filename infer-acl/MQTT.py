# MQTT functions go here (publish, subscribe, etc.)

import paho.mqtt.client as paho


connected = False
successfultopics = set([])


def create_client(username, password):
    print("Creating client")
    client = paho.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.username_pw_set(username, password)

    return client


def client_connect(client, host, port):
    print("Connecting to host")
    client.connect(host, port)


def on_message(client, userdata, msg):
    print("In On_message!")
    print("Topic: ", msg.topic, " Message: ", str(msg.payload))
    successfultopics.add(msg.topic)
    print("List of successful topics is now: ", successfultopics)


def on_connect(client, userdata, flags, rc):
    # print("In On_connect!")
    global connected
    if rc == 0:
        print("Successfully connected")
        connected = True
    else:
        print("Authorization error, wrong password")



def on_publish(client, userdata, mid):
    print("Published message with ID: ", mid)


