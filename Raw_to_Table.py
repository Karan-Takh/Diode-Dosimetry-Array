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
for i in range(1,40):
    m.append(max(df[i]))


print(m)