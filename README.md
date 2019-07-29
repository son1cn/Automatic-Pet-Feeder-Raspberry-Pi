# Automatic Pet Feeder Raspberry Pi
This repo is a design for a 3D printed automatic pet feeder

I started with the 3D model here on thingierse:
https://www.thingiverse.com/thing:2400261

He used an arduino and a few other things, but I had a Raspberry Pi Zero W lying around so decided to use that

Main parts of the design:
3d Printed parts
Raspberry Pi Zero
USB Webcam or RPi camera (optional)
Standard size continuous servo
LED and Light dependent resistor (to know when to stop servo). Part of 3D model

On the RPi Zero:
NodeRed for Webhook relays from IFTTT
Python script to turn servo on and know when done