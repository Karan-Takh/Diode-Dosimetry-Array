from graphviz import Graph

num = input('Enter word: ')

h = Graph('html_table')
h.attr('node', shape='rectangle', bgcolor="brown:green")
h.node('Diode Array', label=f'''<<TABLE>
 <TR>
   <TD>Diode 1</TD>
   <TD>Diode 2</TD>
   <TD>Diode 3</TD>
 </TR>
 <TR>
   <TD>Diode 4</TD>
   <TD>Diode 5</TD>
   <TD>{num}</TD>
 </TR>
</TABLE>>''')

h.view()