from graphviz import Graph
import numpy as np

voltdict = {'diode1': 50, 'diode2': 37, 'diode3': 66, 'diode4': 94, 'diode5': 16,
            'diode6': 51, 'diode7': 45, 'diode8': 100, 'diode9': 39, 'diode10': 64,
            'diode11': 23, 'diode12': 41, 'diode13': 90, 'diode14': 17, 'diode15': 52,
            'diode16': 48, 'diode17': 78, 'diode18': 52, 'diode19': 78, 'diode20': 3}
#
# voltsort = sorted(voltdict.items(), key=lambda voltdict: voltdict[1])
# print(voltsort)
# voltrange = np.linspace(voltsort[0][1], voltsort[19][1], num=9)
# print(list(voltrange))
#
#
#
# for key, value in voltdict:
#     templist = []
#     if voltrange[0] < value < voltrange[1]:
#         templist.append(voltdict[key])
#         templist.append(1)
#         voltdict[key] = templist
#     if voltrange[1] < value < voltrange[2]:
#         templist.append(voltdict[key])
#         templist.append(2)
#         voltdict[key] = templist
#     if voltrange[2] < value < voltrange[3]:
#         templist.append(voltdict[key])
#         templist.append(3)
#         voltdict[key] = templist
#     if voltrange[3] < value < voltrange[4]:
#         templist.append(voltdict[key])
#         templist.append(4)
#         voltdict[key] = templist
#     if voltrange[4] < value < voltrange[5]:
#         templist.append(voltdict[key])
#         templist.append(5)
#         voltdict[key] = templist
#     if voltrange[6] < value < voltrange[7]:
#         templist.append(voltdict[key])
#         templist.append(6)
#         voltdict[key] = templist
#     if voltrange[7] < value < voltrange[8]:
#         templist.append(voltdict[key])
#         templist.append(7)
#         voltdict[key] = templist
#     if voltrange[8] < value < voltrange[9]:
#         templist.append(voltdict[key])
#         templist.append(8)
#         voltdict[key] = templist
#
# print(voltdict)

color = 8

h = Graph('array_table')
h.attr('node', shape='rectangle', bgcolor="brown:green")
h.node('Diode Array', colorscheme='orrd8', label=f'''<<TABLE>
    <TR>
        <TD border="3" bgcolor="{color}">Diode 1</TD>
        <TD>Diode 2</TD>
        <TD>Diode 3</TD>
        <TD>Diode 4</TD>
        <TD>Diode 5</TD>
    </TR>
    <TR>
        <TD>Diode 6: {voltdict['diode6']} V</TD>
        <TD>Diode 7</TD>
        <TD>Diode 8</TD>
        <TD>Diode 9</TD>
        <TD>Diode 10</TD>
    </TR>
    <TR>
        <TD>Diode 11</TD>
        <TD>Diode 12</TD>
        <TD>Diode 13</TD>
        <TD>Diode 14</TD>
        <TD>Diode 15</TD>
    </TR>
    <TR>
        <TD>Diode 16</TD>
        <TD>Diode 17</TD>
        <TD>Diode 18</TD>
        <TD>Diode 19</TD>
        <TD>Diode 20</TD>
    </TR>
</TABLE>>''')

h.view()