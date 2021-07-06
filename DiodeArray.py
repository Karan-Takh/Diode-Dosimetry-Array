from graphviz import Graph

volt6 = 7

h = Graph('html_table')
h.attr('node', shape='rectangle', bgcolor="brown:green")
h.node('Diode Array', label=f'''<<TABLE>
 <TR>
   <TD border="3" style="radial" bgcolor="yellow"  gradientangle="60">Diode 1</TD>
   <TD>Diode 2</TD>
   <TD>Diode 3</TD>
 </TR>
 <TR>
   <TD>Diode 4</TD>
   <TD>Diode 5</TD>
   <TD>Diode 6: {volt6} V</TD>
 </TR>
</TABLE>>''')

h.view()