#!/usr/bin/env python
import os, sys, time
from time import strftime

while True:
    try:
        ret = os.popen('ps -C nginx -o pid,cmd').readlines()
        if len(ret) <2:
            os.system("service nginx start")
            sys.exit(0)

    except Exception as ex:
        print (strftime("%Y-%m-%r %H:%M"))
        sys.exit(0)