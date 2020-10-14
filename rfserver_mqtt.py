#!/usr/bin/python3

import sys, os

# Add path to pyRadioHeadiRF95 module
sys.path.append(os.path.dirname(__file__) + "/../")

import pyRadioHeadRF95 as radio
import paho.mqtt.client as mqtt
import time

rf95 = radio.RF95()

rf95.init()

rf95.setTxPower(14, False)
rf95.setFrequency(915)
def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected with result code:"+str(rc))
    # subscribe for all devices of user
    client.subscribe("parkinglock/motor")



print ("Booting Done!")
print ("Finding Node...")
username = "4179e8c0-0df1-11eb-883c-638d8ce4c23d"
password = "4a5739d0db6c6c224e0bf54b35a6f64a83cb287a"
clientid = "8db30050-0df1-11eb-8779-7d56e82df461"
mqttc = mqtt.Client(client_id=clientid)
mqttc.username_pw_set(username, password=password)
mqttc.connect("mqtt.mydevices.com", 1883, 60)
mqttc.loop_start()
topic_pl = ("parkinglock/"+username+"motor/" +clientid+"/data/1")#publish



#while True:
#waiting to recieve status from the node 
while True:
    if rf95.available():
        print ("Node Found")
        (msg, l) = rf95.recv()
        
        print ("Received Status: " + str(msg) + " (" + str(1) + ")") 
        mqttc.publish(topic_pl, str(msg), True)
        time.sleep(0.5)
#sending command data to Node(Arduino)
#        msg = input("Sending Command : ")
 #       rf95.send(bytes(msg, "utf-8" ),l)
        
 #       rf95.waitPacketSent()
  #      time.sleep(1)
   # else:
    #    time.sleep(0.5)


