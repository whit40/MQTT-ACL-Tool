# Main file
import MQTT
import time
from parser_input import parse_args
import sys


def main(argv):
    print("Hello World!")

    # process user input here
    username, password, topiclist, hostname = parse_args(argv)

    client = MQTT.create_client(username, password)

    MQTT.client_connect(client, hostname, 1883)

    client.subscribe("#")

    for topic in topiclist:
        message = "This message is from topic: " + topic
        client.subscribe(topic)
        client.publish(topic, message, qos=0, retain=False)

    client.loop_forever()
    client.disconnect()


if __name__ == "__main__":
    main(sys.argv[1:])

