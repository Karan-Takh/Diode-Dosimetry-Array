# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nidaqmx as ni

header = "Dev1/ai"
channels = []

for i in range(0,8):
    channels.append(header+str(i))
    
for i in channels:
    with ni.Task() as task:
        task.ai_channels.add_ai_voltage_chan(i)
        print(i + ": " + str(task.read()))
    
