# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import nidaqmx as ni

# Header is just the device string, the number j is which device(Dev1 - Dev5), the number i is which port on the device (ai0 - ai7)
header = "Dev"
address= "/ai"
channels = []
data = [0]*15

#Creates the names for each channel (all 40)
for j in range(1,6):
    for i in range(0,8):
        channels.append(header+str(j)+address+str(i))

#Creates empty dataframe
dataframe = pd.DataFrame()



#Starts a loop ofr each channel, for each channel takes 15 measurements and saves it into an array, after it takes all 15
# it loads the array into the dataframe and starts again
for i in channels:
    j = 0
    while j < 15:
        with ni.Task() as task:
            task.ai_channels.add_ai_voltage_chan(i)
            data[j] = (task.read())
            j+=1
    dataframe.insert(0,i,data)   #would be nice to make this so that the dataframe prints from Dev1/ai0 -> Dev5/ai7 but 
                                 #But it currently goes the other way 
    
    