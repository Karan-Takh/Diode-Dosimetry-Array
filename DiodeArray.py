from graphviz import Graph
import numpy as np

voltdict = {'diode1': 50, 'diode2': 37, 'diode3': 66, 'diode4': 94, 'diode5': 16,
            'diode6': 51, 'diode7': 45, 'diode8': 100, 'diode9': 39, 'diode10': 64,
            'diode11': 23, 'diode12': 41, 'diode13': 90, 'diode14': 17, 'diode15': 52,
            'diode16': 48, 'diode17': 78, 'diode18': 52, 'diode19': 78, 'diode20': 3}


voltsort = sorted(voltdict.items(), key=lambda voltdict: voltdict[1])
print(voltsort)
voltrange = np.linspace(voltsort[0][1], voltsort[19][1], num=10)
print(list(voltrange))

colordict = {}

for key in voltdict.keys():
    templist = []
    if voltrange[0] <= voltdict[key] < voltrange[1]:
        templist.append(voltdict[key])
        templist.append(1)
        templist.append('black')
        colordict[key] = templist
    elif voltrange[1] <= voltdict[key] < voltrange[2]:
        templist.append(voltdict[key])
        templist.append(2)
        templist.append('black')
        colordict[key] = templist
    elif voltrange[2] <= voltdict[key] < voltrange[3]:
        templist.append(voltdict[key])
        templist.append(3)
        templist.append('black')
        colordict[key] = templist
    elif voltrange[3] <= voltdict[key] < voltrange[4]:
        templist.append(voltdict[key])
        templist.append(4)
        templist.append('black')
        colordict[key] = templist
    elif voltrange[4] <= voltdict[key] <= voltrange[5]:
        templist.append(voltdict[key])
        templist.append(5)
        templist.append('black')
        colordict[key] = templist
    elif voltrange[5] < voltdict[key] <= voltrange[6]:
        templist.append(voltdict[key])
        templist.append(6)
        templist.append('white')
        colordict[key] = templist
    elif voltrange[6] < voltdict[key] <= voltrange[7]:
        templist.append(voltdict[key])
        templist.append(7)
        templist.append('white')
        colordict[key] = templist
    elif voltrange[7] < voltdict[key] <= voltrange[8]:
        templist.append(voltdict[key])
        templist.append(8)
        templist.append('white')
        colordict[key] = templist
    elif voltrange[8] < voltdict[key] <= voltrange[9]:
        templist.append(voltdict[key])
        templist.append(9)
        templist.append('white')
        colordict[key] = templist
    else: print(voltdict[key], 'is out of range')

print(colordict)

h = Graph('array_table')
h.attr('node', shape='rectangle')
h.node('Diode Array', colorscheme='orrd9', label=f'''<<TABLE>
    <TR>
        <TD bgcolor="{colordict['diode1'][1]}"><FONT COLOR="{colordict['diode1'][2]}">Diode 1: {voltdict['diode1']} V</FONT></TD>
        <TD bgcolor="{colordict['diode2'][1]}"><FONT COLOR="{colordict['diode2'][2]}">Diode 2: {voltdict['diode2']} V</FONT></TD>
        <TD bgcolor="{colordict['diode3'][1]}"><FONT COLOR="{colordict['diode3'][2]}">Diode 3: {voltdict['diode3']} V</FONT></TD>
        <TD bgcolor="{colordict['diode4'][1]}"><FONT COLOR="{colordict['diode4'][2]}">Diode 4: {voltdict['diode4']} V</FONT></TD>
        <TD bgcolor="{colordict['diode5'][1]}"><FONT COLOR="{colordict['diode5'][2]}">Diode 5: {voltdict['diode5']} V</FONT></TD>
    </TR>
    <TR>
        <TD bgcolor="{colordict['diode6'][1]}"><FONT COLOR="{colordict['diode6'][2]}">Diode 6: {voltdict['diode6']} V</FONT></TD>
        <TD bgcolor="{colordict['diode7'][1]}"><FONT COLOR="{colordict['diode7'][2]}">Diode 7: {voltdict['diode7']} V</FONT></TD>
        <TD bgcolor="{colordict['diode8'][1]}"><FONT COLOR="{colordict['diode8'][2]}">Diode 8: {voltdict['diode8']} V</FONT></TD>
        <TD bgcolor="{colordict['diode9'][1]}"><FONT COLOR="{colordict['diode9'][2]}">Diode 9: {voltdict['diode9']} V</FONT></TD>
        <TD bgcolor="{colordict['diode10'][1]}"><FONT COLOR="{colordict['diode10'][2]}">Diode 10: {voltdict['diode10']} V</FONT></TD>
    </TR>
    <TR>
        <TD bgcolor="{colordict['diode11'][1]}"><FONT COLOR="{colordict['diode11'][2]}">Diode 11: {voltdict['diode11']} V</FONT></TD>
        <TD bgcolor="{colordict['diode12'][1]}"><FONT COLOR="{colordict['diode12'][2]}">Diode 12: {voltdict['diode12']} V</FONT></TD>
        <TD bgcolor="{colordict['diode13'][1]}"><FONT COLOR="{colordict['diode13'][2]}">Diode 13: {voltdict['diode13']} V</FONT></TD>
        <TD bgcolor="{colordict['diode14'][1]}"><FONT COLOR="{colordict['diode14'][2]}">Diode 14: {voltdict['diode14']} V</FONT></TD>
        <TD bgcolor="{colordict['diode15'][1]}"><FONT COLOR="{colordict['diode15'][2]}">Diode 15: {voltdict['diode15']} V</FONT></TD>
    </TR>
    <TR>
        <TD bgcolor="{colordict['diode16'][1]}"><FONT COLOR="{colordict['diode16'][2]}">Diode 16: {voltdict['diode16']} V</FONT></TD>
        <TD bgcolor="{colordict['diode17'][1]}"><FONT COLOR="{colordict['diode17'][2]}">Diode 17: {voltdict['diode17']} V</FONT></TD>
        <TD bgcolor="{colordict['diode18'][1]}"><FONT COLOR="{colordict['diode18'][2]}">Diode 18: {voltdict['diode18']} V</FONT></TD>
        <TD bgcolor="{colordict['diode19'][1]}"><FONT COLOR="{colordict['diode19'][2]}">Diode 19: {voltdict['diode19']} V</FONT></TD>
        <TD bgcolor="{colordict['diode20'][1]}"><FONT COLOR="{colordict['diode20'][2]}">Diode 20: {voltdict['diode20']} V</FONT></TD>
    </TR>
</TABLE>>''')

h.view()