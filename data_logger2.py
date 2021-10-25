# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import nidaqmx as ni
from graphviz import Graph
import numpy as np
# from nidaqmx.constants import LineGrouping
from nidaqmx.constants import Edge
from nidaqmx.constants import AcquisitionType

### Initializing Things ###
# Header is just the device string, the number j is which device(Dev1 - Dev5), the number i is which port on the device (ai0 - ai7)
header = "Dev"
address= "/ai"
channels = []
data = [0]*100000
MVolt = []
IntVolt = []
names = []


# Set the start of enumerated loop below, s, equal to 0.
s = 0
# Outermost loop to loop through each pxi device as a separate task. 
for j in range(1,6):
    # Make a separate list for the channels of the specific device we are dealing with
    current_chans = []
    task = ni.Task("Dev"+str(j))
    # print("The task is Dev" + str(j))
    # task = "Dev" + str(j)
    # with ni.Task() as task:
    for i in range(0,8):
        channels.append(header+str(j)+address+str(i))
        # Add headers to the current channels list too. It should be empty by this step in each loop through j. 
        current_chans.append(header+str(j)+address+str(i))
        task.ai_channels.add_ai_voltage_chan(header+str(j)+address+str(i))
            

    # Creates empty dataframe
    dataframe = pd.DataFrame()
    # pd.set_option('display.max_columns', None) # prevents trailing elipses

    task.timing.cfg_samp_clk_timing(2500000, active_edge=Edge.RISING,sample_mode=AcquisitionType.FINITE,samps_per_chan=100000)
    
    # Starts a loop for each channel, for each channel takes 1 mil measurements and saves it into an array, after it takes all million
    # it loads the array into the dataframe and starts again
    for count, i in enumerate(current_chans, start=s):
        # print("start is", s)
        # print("For channel:", i)
        k = 0
        # Add start and stop to try to improve performance. (unsure where each of these statements would best go)
        task.start()
        while k < len(data):
            data[k] = (task.read())
            k+=1
        task.stop()
        # print(data)
        # create separate list for the data for the specific channel which we are concerned with. 'Count' is the numbered iteration of the for loop (https://stackoverflow.com/questions/25050311/extract-first-item-of-each-sublist)
        # print('count is', count)
        channel_data = [item[count-s] for item in data]
        # print("Full data is", data)
        # print("channel data for channel", i, ":\n", channel_data)
        # print(max(channel_data))
        MVolt.append(round(max(channel_data),5))                            # These look very different when the voltages are around 4V but are roughly the same when the channels
        IntVolt.append(sum(channel_data))                                   # are correctly calibrated 
        dataframe.insert(len(dataframe.columns),i,channel_data)             # would be nice to make this so that the dataframe prints from Dev1/ai0 -> Dev5/ai7 but 
                                                                            # But it currently goes the other way
    # Add 8 to s, so the next count starts at                           
    s += 8                                                              
                                                                
    task.close()
        
   
# print(dataframe)

### Creates Secondary Array for Ease of Access ###
types = ["Int","Max"]    
voltframe = pd.DataFrame(index = types,columns = channels)
# vframe_length = len(voltframe)
voltframe.loc[types[0]] = IntVolt 
voltframe.loc[types[1]] = MVolt

### Creates List of Names and a dictionary as used in Karen's Code ###
for i in range(1,41):
    names.append("diode"+str(i))


voltdict = dict(zip(names,MVolt))       # Used MVolt and not IntVolt as it seemed more accurate (for now)


####################################################################################################################

# KARENS STUFF

###################################################################################################################

# Takes the lowest and highest voltage values and creates 22 equal intervals between these values
voltsort = sorted(voltdict.items(), key=lambda voltdict: voltdict[1])
voltrange = np.linspace(voltsort[0][1], voltsort[33][1], num=22)

# print('Intervals:', list(voltrange))  --- Don't print; will get crazy as we're doing million samples

# Assigns cell and font color based on the value of the voltage
colordict = {}
for key in voltdict.keys():
    templist = []
    if voltrange[0] <= voltdict[key] < voltrange[1]:
        templist.append(voltdict[key])
        templist.append('#ffffff')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[1] <= voltdict[key] < voltrange[2]:
        templist.append(voltdict[key])
        templist.append('#ffe6e6')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[2] <= voltdict[key] < voltrange[3]:
        templist.append(voltdict[key])
        templist.append('#ffcccc')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[3] <= voltdict[key] < voltrange[4]:
        templist.append(voltdict[key])
        templist.append('#ffb3b3')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[4] <= voltdict[key] <= voltrange[5]:
        templist.append(voltdict[key])
        templist.append('#ff9999')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[5] < voltdict[key] <= voltrange[6]:
        templist.append(voltdict[key])
        templist.append('#ff8080')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[6] < voltdict[key] <= voltrange[7]:
        templist.append(voltdict[key])
        templist.append('#ff6666')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[7] < voltdict[key] <= voltrange[8]:
        templist.append(voltdict[key])
        templist.append('#ff4d4d')
        templist.append('black')
        colordict[key] = templist
    elif voltrange[8] < voltdict[key] <= voltrange[9]:
        templist.append(voltdict[key])
        templist.append('#ff3333')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[9] < voltdict[key] <= voltrange[10]:
        templist.append(voltdict[key])
        templist.append('#ff1a1a')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[10] < voltdict[key] <= voltrange[11]:
        templist.append(voltdict[key])
        templist.append('#ff0000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[11] < voltdict[key] <= voltrange[12]:
        templist.append(voltdict[key])
        templist.append('#e60000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[12] < voltdict[key] <= voltrange[13]:
        templist.append(voltdict[key])
        templist.append('#cc0000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[13] < voltdict[key] <= voltrange[14]:
        templist.append(voltdict[key])
        templist.append('#b30000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[14] < voltdict[key] <= voltrange[15]:
        templist.append(voltdict[key])
        templist.append('#990000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[15] < voltdict[key] <= voltrange[16]:
        templist.append(voltdict[key])
        templist.append('#800000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[16] < voltdict[key] <= voltrange[17]:
        templist.append(voltdict[key])
        templist.append('#660000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[17] < voltdict[key] <= voltrange[18]:
        templist.append(voltdict[key])
        templist.append('#4d0000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[18] < voltdict[key] <= voltrange[19]:
        templist.append(voltdict[key])
        templist.append('#330000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[19] < voltdict[key] <= voltrange[20]:
        templist.append(voltdict[key])
        templist.append('#1a0000')
        templist.append('white')
        colordict[key] = templist
    elif voltrange[20] < voltdict[key] <= voltrange[21]:
        templist.append(voltdict[key])
        templist.append('#000000')
        templist.append('white')
        colordict[key] = templist
    else:
        # print(voltdict[key], 'is out of range')
        templist.append(voltdict[key])
        templist.append('#0000ff')
        templist.append('white')
        colordict[key] = templist

print('Assigned Colors:', colordict)

# Creates test table for the 8 diodes
# h = Graph('test_table')
# h.attr('node', shape='rectangle')
# h.node('Diode Array', label=f'''<<TABLE cellspacing="10">
#     <TR>
#          <TD bgcolor="{colordict['diode1'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode1'][2]}">Diode 1 <BR align="center" /> {voltdict['diode1']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode14'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode14'][2]}">Diode 2 <BR align="center" /> {voltdict['diode14']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode22'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode22'][2]}">Diode 3 <BR align="center" /> {voltdict['diode22']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode30'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode30'][2]}">Diode 4 <BR align="center" /> {voltdict['diode30']} V</FONT></TD>
#     </TR>
#
# </TABLE>>''')


    # <TR>
    #      <TD bgcolor="{colordict['diode5'][1]}" fixedsize="true" width="70"
    #     height="70"><FONT COLOR="{colordict['diode5'][2]}">Diode 5 <BR align="center" /> {voltdict['diode5']} V</FONT></TD>
    #     <TD bgcolor="{colordict['diode6'][1]}" fixedsize="true" width="70"
    #     height="70"><FONT COLOR="{colordict['diode6'][2]}">Diode 6 <BR align="center" /> {voltdict['diode6']} V</FONT></TD>
    #     <TD bgcolor="{colordict['diode7'][1]}" fixedsize="true" width="70"
    #     height="70"><FONT COLOR="{colordict['diode7'][2]}">Diode 7 <BR align="center" /> {voltdict['diode7']} V</FONT></TD>
    #     <TD bgcolor="{colordict['diode8'][1]}" fixedsize="true" width="70"
    #     height="70"><FONT COLOR="{colordict['diode8'][2]}">Diode 8 <BR align="center" /> {voltdict['diode8']} V</FONT></TD>
    # </TR>

# Creates the table (Please don't edit any of the code below)
h = Graph('array_table')
h.attr('node', shape='rectangle')
h.node('Diode Array', label=f'''<<TABLE cellspacing="10">
    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode37'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode37'][2]}">Diode 37 <BR align="center" /> {voltdict['diode37']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode1'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode1'][2]}">Diode 1 <BR align="center" /> {voltdict['diode1']} V</FONT></TD>

        <TD bgcolor="{colordict['diode2'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode2'][2]}">Diode 2 <BR align="center" /> {voltdict['diode2']} V</FONT></TD>

        <TD bgcolor="{colordict['diode3'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode3'][2]}">Diode 3 <BR align="center" /> {voltdict['diode3']} V</FONT></TD>

        <TD bgcolor="{colordict['diode4'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode4'][2]}">Diode 4 <BR align="center" /> {voltdict['diode4']} V</FONT></TD>

        <TD bgcolor="{colordict['diode5'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode5'][2]}">Diode 5 <BR align="center" /> {voltdict['diode5']} V</FONT></TD>

        <TD bgcolor="{colordict['diode6'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode6'][2]}">Diode 6 <BR align="center" /> {voltdict['diode6']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode7'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode7'][2]}">Diode 7 <BR align="center" /> {voltdict['diode7']} V</FONT></TD>

        <TD bgcolor="{colordict['diode8'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode8'][2]}">Diode 8 <BR align="center" /> {voltdict['diode8']} V</FONT></TD>

        <TD bgcolor="{colordict['diode9'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode9'][2]}">Diode 9 <BR align="center" /> {voltdict['diode9']} V</FONT></TD>

        <TD bgcolor="{colordict['diode10'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode10'][2]}">Diode 10 <BR align="center" /> {voltdict['diode10']} V</FONT></TD>

        <TD bgcolor="{colordict['diode11'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode11'][2]}">Diode 11 <BR align="center" /> {voltdict['diode11']} V</FONT></TD>

        <TD bgcolor="{colordict['diode12'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode12'][2]}">Diode 12 <BR align="center" /> {voltdict['diode12']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode13'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode13'][2]}">Diode 13 <BR align="center" /> {voltdict['diode13']} V</FONT></TD>

        <TD bgcolor="{colordict['diode14'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode14'][2]}">Diode 14 <BR align="center" /> {voltdict['diode14']} V</FONT></TD>

        <TD bgcolor="{colordict['diode15'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode15'][2]}">Diode 15 <BR align="center" /> {voltdict['diode15']} V</FONT></TD>

        <TD bgcolor="{colordict['diode16'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode16'][2]}">Diode 16 <BR align="center" /> {voltdict['diode16']} V</FONT></TD>

        <TD bgcolor="{colordict['diode17'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode17'][2]}">Diode 17 <BR align="center" /> {voltdict['diode17']} V</FONT></TD>

        <TD bgcolor="{colordict['diode18'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode18'][2]}">Diode 18 <BR align="center" /> {voltdict['diode18']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="{colordict['diode38'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode38'][2]}">Diode 38 <BR align="center" /> {voltdict['diode38']} V</FONT></TD>

        <TD bgcolor="{colordict['diode19'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode19'][2]}">Diode 19 <BR align="center" /> {voltdict['diode19']} V</FONT></TD>

        <TD bgcolor="{colordict['diode20'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode20'][2]}">Diode 20 <BR align="center" /> {voltdict['diode20']} V</FONT></TD>

        <TD bgcolor="{colordict['diode21'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode21'][2]}">Diode 21 <BR align="center" /> {voltdict['diode21']} V</FONT></TD>

        <TD bgcolor="{colordict['diode22'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode22'][2]}">Diode 22 <BR align="center" /> {voltdict['diode22']} V</FONT></TD>

        <TD bgcolor="{colordict['diode23'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode23'][2]}">Diode 23 <BR align="center" /> {voltdict['diode23']} V</FONT></TD>

        <TD bgcolor="{colordict['diode24'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode24'][2]}">Diode 24 <BR align="center" /> {voltdict['diode24']} V</FONT></TD>

        <TD bgcolor="{colordict['diode39'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode39'][2]}">Diode 39 <BR align="center" /> {voltdict['diode39']} V</FONT></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode25'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode25'][2]}">Diode 25 <BR align="center" /> {voltdict['diode25']} V</FONT></TD>

        <TD bgcolor="{colordict['diode26'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode26'][2]}">Diode 26 <BR align="center" /> {voltdict['diode26']} V</FONT></TD>

        <TD bgcolor="{colordict['diode27'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode27'][2]}">Diode 27 <BR align="center" /> {voltdict['diode27']} V</FONT></TD>

        <TD bgcolor="{colordict['diode28'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode28'][2]}">Diode 28 <BR align="center" /> {voltdict['diode28']} V</FONT></TD>

        <TD bgcolor="{colordict['diode29'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode29'][2]}">Diode 29 <BR align="center" /> {voltdict['diode29']} V</FONT></TD>

        <TD bgcolor="{colordict['diode30'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode30'][2]}">Diode 30 <BR align="center" /> {voltdict['diode30']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode31'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode31'][2]}">Diode 31 <BR align="center" /> {voltdict['diode31']} V</FONT></TD>

        <TD bgcolor="{colordict['diode32'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode32'][2]}">Diode 32 <BR align="center" /> {voltdict['diode32']} V</FONT></TD>

        <TD bgcolor="{colordict['diode33'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode33'][2]}">Diode 33 <BR align="center" /> {voltdict['diode33']} V</FONT></TD>

        <TD bgcolor="{colordict['diode34'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode34'][2]}">Diode 34 <BR align="center" /> {voltdict['diode34']} V</FONT></TD>

        <TD bgcolor="{colordict['diode35'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode35'][2]}">Diode 35 <BR align="center" /> {voltdict['diode35']} V</FONT></TD>

        <TD bgcolor="{colordict['diode36'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode36'][2]}">Diode 36 <BR align="center" /> {voltdict['diode36']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>


    <TR>
        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="{colordict['diode40'][1]}" fixedsize="true" width="70"
        height="70"><FONT COLOR="{colordict['diode40'][2]}">Diode 40 <BR align="center" /> {voltdict['diode40']} V</FONT></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>

        <TD bgcolor="#cccccc" fixedsize="true" width="70" height="70"></TD>
    </TR>
</TABLE>>''')

h.view()
