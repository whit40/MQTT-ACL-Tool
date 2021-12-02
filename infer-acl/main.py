# Main file
import MQTT
from parser_input import parse_args
import sys


def main(argv):

    # process user input here
    username, password, topiclist, hostname = parse_args(argv)

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
    main(sys.argv[1:])

