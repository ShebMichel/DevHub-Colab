'''
DevHub Colab Thursday, Jan 9, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''

## example 1
## The objective of this exercise is to use module time in python
# 1- import module
import time
# 2- run the event 3 times
for a in range(3):
    # Get the current time
    current_time = time.strftime("%H:%M:%S", time.localtime())
    #print("The banch length changes width =", d)
    print("What is the time now =", current_time)
    print("Once upon a time...")
    time.sleep(2)
    print("A little robot appeared:")
    print("  [o_o]")
    
    ##
    # Get the current time in UTC
    utc_time = time.gmtime()
    
    # Offset for AWST is UTC+8
    awst_offset_seconds = 8 * 60 * 60  # 8 hours in seconds
    awst_time = time.gmtime(time.mktime(utc_time) + awst_offset_seconds)
    print(awst_time)
    # Format and print the time in AWST
    print("Current Time in AWST:", time.strftime("%Y-%m-%d %H:%M:%S", awst_time))
 
    time.sleep(2)
    print("And it said, 'Hello, world!'")