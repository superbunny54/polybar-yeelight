#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Funct import *
import time
if os.path.exists("/tmp/.checkrun"):
    print("an instance is already running")
    exit()


else:
    try:
        File("Create")
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
    finally:
        File("Remove")
