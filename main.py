# Main file
import MQTT
import time

topiclist = ["test/message1", "test/message2", "blah/message"]


def main():
    print("Hello World!")

    # process user input here

    # will need to set user/pass manually for now
    client = MQTT.create_client("user", "password")


    # will need to change hostname manually for now
    MQTT.client_connect(client, "mqttserver", 1883)

    for topic in topiclist:
        message = "This message is from topic: " + topic
        client.subscribe(topic)
        client.publish(topic, message, qos=0, retain=False)

    client.loop_forever()
    client.disconnect()


if __name__ == "__main__":
    main()

