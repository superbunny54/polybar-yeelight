#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from yeelight import *
import time
# Put the ip address of your lamp here

IPAddress = "192.168.1.12"
Bulb = Bulb(IPAddress)
arg = sys.argv[1]


##########################################################################
# This function write the state to a file for dynamic change in the bar.
def State(msg):
    File = open("/tmp/State","w")
    File.write(msg)
    
# This function prevent multiple instance from runing at the same time.
def File(state):
    if state == "Create" and not os.path.exists("/tmp/.checkrun"):
        os.mknod("/tmp/.checkrun")
    elif state == "Remove":
        os.remove("/tmp/.checkrun")


# This function get the propreties of your lamp
def Get(argument):
    prop = []
    try:
        prop = Bulb.get_properties()
    except BulbException:
        print("error or quota exceeded")
        exit()
    finally:
        time.sleep(0.1) # prevent to many request per second
    return prop[argument]


##########################################################################
# This function toogle the power state of your lamp 
def Power():
    pwr = Get("power")
    if pwr == "off":
        Bulb.turn_on(effect="smooth", duration=1000)
        State("on")

    elif pwr == "on":
        Bulb.turn_off(effect="smooth", duration=1000)
        State("off")

# This function increase the brightness of your lamp 
def BrPlus():
    Br = Get("bright")
    Br = int(Br)
    if Br == 100:
        exit()
    elif Br < 90:
        Bulb.set_brightness(Br + 10)
    elif Br >= 90 and Br != 100:
        Bulb.set_brightness(100)


# This function decrease the brightness of your lamp 
def BrMinus():
    Br = Get("bright")
    Br = int(Br)
    if Br == 1:
        exit()
    elif Br > 10:
        Bulb.set_brightness(Br - 10)
    elif Br <= 10 and Br != 0:
        Bulb.set_brightness(1)


# This function increase the color temperature of your lamp 
def CtPlus():
    Ct = Get("ct")
    Ct = int(Ct)
    if Ct == 5000:
        exit()
    elif Ct <= 4760:
        Bulb.set_color_temp(Ct + 240)
    else:
        Bulb.set_color_temp(5000)


# This function decrease the color temperature of your lamp 
def CtMinus():
    Ct = Get("ct")
    Ct = int(Ct)
    if Ct == 2600:
        exit()
    elif Ct >= 2840:
        Bulb.set_color_temp(Ct - 240)
    else:
        Bulb.set_color_temp(2600)

