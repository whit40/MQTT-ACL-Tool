import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connection status", rc)
    #rc = 5 indicates auth erro (Wrong username)
    #rc = 0 indicates success (connection success)
    


#Client(client_id=”cl1”, clean_session=True, userdata=None, protocol=MQTTv311, transport=”tcp”)
client =mqtt.Client()
server = "172.16.208.110"
client.username_pw_set(username="abcd",password="1235")
client.on_connect = on_connect
print("Connecting to",server)
client.loop_start()
#client.connect(host, port=1883, keepalive=60, bind_address="")
client.connect(server)
client.publish("test", payload="Hollaaa", qos=0, retain=False)
time.sleep(3)
client.loop_stop()
client.disconnect()
