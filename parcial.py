from lark import Lark, Tree
from lark.tree import pydot__tree_to_png

with open("gramatica.lark") as f:
    grammar = f.read()

parser = Lark(grammar, start="programa")


codigo1 = """
INICIO:
VAR n ENTERO = + 3 4;
VAR y BOOLEANO = VERDADERO; 
SI: < x 10 ENTONCES:
    VAR z BOOLEANO = FALSO;
SINO:
    VAR z BOOLEANO = VERDADERO;
    ;
FIN
"""

codigo = """
INICIO:
VAR a ENTERO = 12;
VAR b ENTERO = 7;
VAR max ENTERO = a;

SI: < b a ENTONCES:
    max = a;
SINO:
    max = b;
;

SALIDA: max;
FIN
"""
codigo2 = """
INICIO:
VAR x ENTERO = 10;
VAR y BOOLEANO = VERDADERO;
VAR z BOOLEANO = & y > x 0;
y = 10;
x = - y 5;
VAR resultado ENTERO = 0;
VAR condicion BOOLEANO = > y x;
SI: & condicion z ENTONCES:
    resultado = 1;
SINO:
    resultado = 2;
;
VAR contador ENTERO = 0;
MIENTRAS: > x 0 HACER:
    contador = + contador 1;
    x = - x 1;
;
SALIDA: contador;
SALIDA: + contador 5;
SALIDA: < contador 0;
FIN
"""
tree = parser.parse(codigo)
#print(tree.pretty())
pydot__tree_to_png(tree, "src/tp_final/mayor_entre_dos.png")