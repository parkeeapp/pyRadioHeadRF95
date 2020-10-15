#!/usr/bin/python3

import sys, os

# Add path to pyRadioHeadiRF95 module
sys.path.append(os.path.dirname(__file__) + "/../")

import pyRadioHeadRF95 as radio
import paho.mqtt.client as mqtt
import time
import logging

rf95 = radio.RF95()

rf95.init()

rf95.setTxPower(14, False)
rf95.setFrequency(915)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    Subs = ("PKE001")
    client.subscribe(Subs)
    print(Subs)

def on_message(client, userdata, msg):
#sending command data to Node(Arduino)
    print("ON MESSAGE")
    print("Message received-> " + msg.topic + " " + str(msg.payload))
#    logging.debug(client);
    print(msg)
    command = msg.payload.decode("utf-8")
    rf95.send(bytes(command, "utf-8" ),l)
    
    rf95.waitPacketSent()
    time.sleep(1)
 

print ("Booting Done!")
print ("Finding Node...")
client = mqtt.Client()
client.connect("mqtt-staging.parkee.app", 1883, 60)
client.on_connect = on_connect
print("SOMETHING")

while True:
    client.loop_start()
    #print("BEFORE LOOP START")
    #print("AFTER LOOP START")
    client.on_message = on_message
    #print("END LINE")
    #waiting to recieve status from the node
    if rf95.available():
        print("Node Found")
        (pesan,l) = rf95.recv()
        
        print ("Received Status: " + str(pesan) + " (" + str(1) + ")") 
        
        time.sleep(1)
client.loop_stop()
