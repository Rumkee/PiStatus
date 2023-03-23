# PiStatus
a project to use a Raspberry Pi to control LEDs to indicate on-call status

PiStatus.py
this is a script to run on the RaspberyPi which will tell the LEDs to illuminate specific colours and the Fans to spin at a certain speed by calling the relevant endpoints. 

TeamsStatus.py
this is a script that will create a WebSocket connection to the Teams client, provided the key is valid and will forward any status changes to the PiStatus server.

Gerber Files
this folder contains the schematics for the circuity for the PCB to interface between the Pi and the LEDS/Fans.
