import paho.mqtt.client as mqtt
import time
connected = False


def on_connect(client, userdata, flags, rc):
    global connected
    if(rc==0):
        print("Successfully connected")
        connected = True
    else:
        print("Authorization error, wrong password")
        connected = "False2"
        exit
    #print(client, userdata, flags, rc)
    #print("hi")

def on_publish(client,userdata, mid):
    print("Message published", mid)


#Client(client_id=”cl1”, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client =mqtt.Client()
server = "172.16.208.110"
client.username_pw_set(username="abcd",password="1334")
client.on_connect = on_connect
print("Connecting to",server)
client.on_publish = on_publish
#client.connect(host, port=1883, keepalive=60, bind_address="")
client.connect(server)
client.loop_start()
while(connected != True):
    if(connected == "False2"):
        break
    time.sleep(0.1)
client.publish("test", payload="Hollaaa")
client.publish("test", payload="Heheh")
client.loop_stop()
client.disconnect()


