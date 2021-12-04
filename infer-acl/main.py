import MQTT
from parser_input import parse_args
import sys


def main(argv):

    # Get user input
    username, password, topiclist, hostname = parse_args(argv)

    # Create MQTT client
    client = MQTT.create_client(username, password)

    # Connect to MQTT server
    MQTT.client_connect(client, hostname, 1883)

    # Subscribe to all topics- this allows us to catch topics not specified by user, with the
    # restriction that someone else must send the message to the topic. User can leave program running for
    # a while to find more topics.
    client.subscribe("#")

    # Subscribe to and publish to all specified topics
    for topic in topiclist:
        message = "This message is from topic: " + topic
        client.subscribe(topic)

        # Can't publish to wildcards, so check topic before publishing.
        if '#' not in topic:
            client.publish(topic, message, qos=0, retain=False)


    print("The tool will now start with this list of provided topics:")
    print(topiclist)
    print("After these topics are tried, the tool will keep listening. You may leave it running to find additional"
          " topics, or exit by using ctrl + c.")

    # Keep listening until user exits program.
    client.loop_forever()
    client.disconnect()


if __name__ == "__main__":
    main(sys.argv[1:])

