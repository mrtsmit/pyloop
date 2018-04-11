#!/usr/bin/python
import string
import time


a = 0
while True:
    print("Hello World - " + str(a))
    a += 1
    time.sleep(2)
    if a > 999999:
        a = 1
