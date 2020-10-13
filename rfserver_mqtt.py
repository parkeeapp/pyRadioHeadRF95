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



#print ("Booting Done!")
#print ("Finding Node...")
clientid = "mqttx_7eabb473"
mqttc = mqtt.Client(client_id=clientid)
mqttc.connect("test.mosquitto.org", port=1883, keepalive=60)
mqttc.loop_start()
topic_pl = ("parkinglock/motor")#publish



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
        msg = input("Sending Command : ")
        rf95.send(bytes(msg, "utf-8" ),l)
        
        rf95.waitPacketSent()
        time.sleep(1)
    else:
        time.sleep(0.5)


