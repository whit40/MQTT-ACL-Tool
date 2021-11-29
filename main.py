# Main file
import MQTT

def main():
    print("Hello World!")

    # will need to set user/pass manually for now
    client = MQTT.create_client("user", "password")

    # will need to change hostname manually for now
    MQTT.client_connect(client, "mqttserver", 1883)

    client.loop_forever()



if __name__ == "__main__":
    main()

