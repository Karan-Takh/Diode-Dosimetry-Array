# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import nidaqmx as ni

header = "Dev1/ai"
channels = []


for i in range(0,8):
    channels.append(header+str(i))

# Create dataframe with channels as indices (maybe channels has to be in brackets?)
dataframe = pd.DataFrame(index=channels)

for j in range(0,9):
    for i in channels:
        with ni.Task() as task:
            task.ai_channels.add_ai_voltage_chan(i)
            print(i + ": " + str(task.read()))
            
