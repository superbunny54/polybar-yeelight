#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from yeelight import *
import time

# This function get the propreties of your lamp
def Get(argument):
    prop = []
    try:
        prop = Bulb.get_properties()
    except BulbException:
        print("quota exceeded")
        exit()
    return (prop[argument])


# This function toogle the power state of your lamp 
def Power():
    pwr = Get("power")
    if pwr == "off":
        Bulb.turn_on(effect="smooth", duration=1000)
    elif pwr == "on":
        Bulb.turn_off(effect="smooth", duration=1000)


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

#################################################
# Put the ip address of your lamp here ##########
IPAddress = "192.168.1.12"
#################################################

Bulb = Bulb(IPAddress)
arg = sys.argv[1]
if arg == "pwr":
    Power()
    exit()
elif arg == "brplus":
    BrPlus()
    exit()
elif arg == "brminus":
    BrMinus()
    exit()
elif arg == "ctplus":
    CtPlus()
    exit()
elif arg == "ctminus":
    CtMinus()
    exit()
