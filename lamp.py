#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Funct import *
import time
try:
    State = open("/tmp/State","r")
except:
    os.mknod("/tmp/State")



if os.path.exists("/tmp/.checkrun"):
    print("running")

else:
    print(State.read())
    try:
        if arg == "pwr":
            File("Create")
            out = Power()

        elif arg == "brplus":
            File("Create")
            BrPlus()

        elif arg == "brminus":
            File("Create")
            BrMinus()

        elif arg == "ctplus":
            File("Create")
            CtPlus()

        elif arg == "ctminus":
            File("Create")
            CtMinus()
  
    finally:
        if os.path.exists("/tmp/.checkrun"):
            File("Remove")
