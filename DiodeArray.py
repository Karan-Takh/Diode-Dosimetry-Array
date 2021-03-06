from graphviz import Graph
import numpy as np

# Sample dictionary of voltages with values between 0 and 100
voltdict = {'diode1': 50.96, 'diode2': 37.130, 'diode3': 66.593, 'diode4': 94.602, 'diode5': 16.279,
            'diode6': 51.617, 'diode7': 45.375, 'diode8': 100.671, 'diode9': 39.795, 'diode10': 64.414,
            'diode11': 23.623, 'diode12': 41.635, 'diode13': 90.643, 'diode14': 17.266, 'diode15': 52.150,
            'diode16': 48.245, 'diode17': 78.973, 'diode18': 52.669, 'diode19': 78.938, 'diode20': 3.696,
            'diode21': 78, 'diode22': 94, 'diode23': 34, 'diode24': 67, 'diode25': 79,
            'diode26': 71, 'diode27': 65, 'diode28': 14, 'diode29': 86, 'diode30': 13,
            'diode31': 93, 'diode32': 21, 'diode33': 55, 'diode34': 83, 'diode35': 67,
            'diode36': 44, 'diode37': 59, 'diode38': 35, 'diode39': 34, 'diode40': 2}

# Takes the lowest and highest voltage values and creates nine equal intervals between these values
voltsort = sorted(voltdict.items(), key=lambda voltdict: voltdict[1])
voltrange = np.linspace(voltsort[0][1], voltsort[39][1], num=22)
print('Intervals:', list(voltrange))

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
        print(voltdict[key], 'is out of range')

print('Assigned Colors:', colordict)

# Creates test table for the 8 diodes
# h = Graph('test_table')
# h.attr('node', shape='rectangle')
# h.node('Diode Array', label=f'''<<TABLE cellspacing="10">
#     <TR>
#          <TD bgcolor="{colordict['diode1'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode1'][2]}">Diode 1 <BR align="center" /> {voltdict['diode1']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode2'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode2'][2]}">Diode 2 <BR align="center" /> {voltdict['diode2']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode3'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode3'][2]}">Diode 3 <BR align="center" /> {voltdict['diode3']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode4'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode4'][2]}">Diode 4 <BR align="center" /> {voltdict['diode4']} V</FONT></TD>
#     </TR>
#
#
#     <TR>
#          <TD bgcolor="{colordict['diode5'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode5'][2]}">Diode 5 <BR align="center" /> {voltdict['diode5']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode6'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode6'][2]}">Diode 6 <BR align="center" /> {voltdict['diode6']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode7'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode7'][2]}">Diode 7 <BR align="center" /> {voltdict['diode7']} V</FONT></TD>
#         <TD bgcolor="{colordict['diode8'][1]}" fixedsize="true" width="70"
#         height="70"><FONT COLOR="{colordict['diode8'][2]}">Diode 8 <BR align="center" /> {voltdict['diode8']} V</FONT></TD>
#     </TR>
# </TABLE>>''')

# Creates the table (Please don't edit any of the code below)
h = Graph('array_table')
# h.node('test')
# h.node_attr['test']='square'
# h.add_node(1, shape='square')
# h.node('4', 'Ni!', shape='square')

# h.node('1',pos='1,2!')
# h.edge('1','2')
# h.attr('node', shape='square')
# h.node('test', **{'width':'1', 'height':'1'})

# h.node('1',pos='0,50!', shape='square')
# h.attr('node', shape='square', fillcolor="#cccccc")
# h.node('test', **{'width':'0.9', 'height':'0.9'}, style='filled')

h.attr('node', shape='rectangle')
h.node('Diode Array', label=f'''<<TABLE cellspacing="10" valign='top'>
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


# h.attr('node', shape='square')
# h.node('test 2', **{'width':'1', 'height':'1'})

# h.attr('node', shape='square')
# h.node('test 2', **{'width':'1', 'height':'1'}, valign='bottom')


h.view()
