# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:38:25 2021

@author: Wil Morrissey
"""

import numpy as np
import pandas as pd

columns = np.arange(1,41)   #Need to change this if we come up with a different naming convention

df = pd.DataFrame(np.random.randint(0,100,size=(100001,40)), columns = columns)   #in the future, this will be replaced with
                                                                                    #importing the data from the diode array into a dataframe
                                                                                    

m = []
answer = str(input("Please Select Method [Max / Integrate]: "))                 #need to select which method of coming up with the value
valids1 = ["Max", "max", "m", "M"]
valids2 = ["Integrate", "integrate", "Sum", "sum", "I", "i", "s", "S"]

i = 1
while i in range(1,40):
    if answer in valids1:    
        m.append(max(df[i]))
    elif answer in valids2:
        m.append(sum(df[i]))
    else:
        print("Please select a valid form of analysis")
        i = 42
print(m)