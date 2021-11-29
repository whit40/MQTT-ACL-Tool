# MQTT functions go here (publish, subscribe, etc.)

import paho.mqtt.client as paho


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


def on_message():
    print("In On_message!")


def on_connect(client,userdata,flags,rc):
    print("In On_connect!")
    payload = "test from ACL tool!"
    client.publish("test/message", payload, qos=0, retain= False)

