import MQTT
from parser_input import parse_args
import listener
import sys


def infer(username, password, topiclist, hostname):

    # process user input here
    #username, password, topiclist, hostname = parse_args(argv)

    client = MQTT.create_client(username, password)

    MQTT.client_connect(client, hostname, 1883)

    client.subscribe("#")

    for topic in topiclist:
        message = "This message is from topic: " + topic
        client.subscribe(topic)
        if '#' not in topic:
            client.publish(topic, message, qos=0, retain=False)


    print("The tool will now start with this list of provided topics:")
    print(topiclist)
    print("After these topics are tried, the tool will keep listening. You may leave it running to find additional"
          " topics, or exit by using ctrl + c.")

    client.loop_forever()
    client.disconnect()


if __name__ == "__main__":
    print("MQTT Smasher tool")
    print("1. listen on network and snipe login info")
    print("2. I have a user info, map the queue permissions for me")
    ch = input()
    if(ch=='2'):
        print("Username")
        username=input()
        print("Password")
        password=input()
        print("Path to the topic file")
        topiclist=input()
        print("MQTT server address")
        hostname=input()
        infer(username, password, topiclist, hostname)
    elif(ch=='1'):
        print("Duration of snipe, in seconds :")
        tim = input()
        listener.sniper(tim)

