
#!/usr/bin/python3

import sys, os

# Add path to pyRadioHeadiRF95 module
sys.path.append(os.path.dirname(__file__) + "/../")

import pyRadioHeadRF95 as radio
import time

rf95 = radio.RF95()

rf95.init()

rf95.setTxPower(14, False)
rf95.setFrequency(915)


#rf95.setSignalBandwidth(rf95.Bandwidth500KHZ)
#rf95.setSpreadingFactor(rf95.SpreadingFactor9)
#rf95.setCodingRate4(rf95.CodingRate4_8)

print ("Booting Done!")
print ("Finding Node...")


while True:

#waiting to recieve status from the node 
    if rf95.available():
        print ("Node Found")
        (msg, l) = rf95.recv()
        print ("Received Status: " + str(msg) + " (" + str(1) + ")") 
        time.sleep(2)
#sending command data to Node(Arduino)
       # print ("Sending Command : ") 
        msg = input("Sending Command : ")
        rf95.send(bytes(msg, "utf-8" ),l)
        
        rf95.waitPacketSent()
        time.sleep(3)
    else:
        time.sleep(1)
