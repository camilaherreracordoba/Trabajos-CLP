from lark import Lark, Transformer, Tree
from lark.tree import pydot__tree_to_png
# Gramática simplificada de Chef en estilo Lark (EBNF)
chef_grammar = r"""
    start: programa

    programa: identificador "." "Ingredients." lista_ingredientes "Method." metodos
            | identificador "." "Ingredients." lista_ingredientes "Method." metodos "Serves" entero "."

    lista_ingredientes: ingrediente+

    ingrediente: entero unidad? identificador

    unidad: seco
          | modificador? (liquido | volumen)

    modificador: "heaped" | "level"
    seco: "g" | "kg" | "pinch"
    liquido: "ml" | "l"
    volumen: "tablespoon" | "teaspoon" | "cup"

    metodos: instruccion+

    instruccion: (instruccion_a_ingrediente
                | "Add" "dry" "ingredients" ("to" recipiente_mezcla)?
                | "Liquefy" ("contents" "of" recipiente_mezcla | identificador)
                | "Stir" ((recipiente_mezcla "for" entero "minutes") 
                         | ("for" entero "minutes") 
                         | (identificador "into" recipiente_mezcla))
                | "Mix" recipiente_mezcla? "well"
                | "Clean" recipiente_mezcla
                | "Pour" "contents" "of" recipiente_mezcla "into" recipiente_horneado
                | "Serve" "with" identificador) "."

    instruccion_a_ingrediente: (("Put" | "Fold") identificador "into" recipiente_mezcla
                              | "Remove" identificador ("from" recipiente_mezcla)?
                              | ("Add" | "Combine" | "Divide") identificador ("into" recipiente_mezcla)?)

    recipiente_mezcla: "the"? ordinal? "mixing" "bowl"
    recipiente_horneado: "the"? ordinal? "baking" "dish"

    ordinal: "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th"

    identificador: (LETRA | NUMERO)+
    entero: NUMERO+

    LETRA: /[A-Za-z]/
    NUMERO: /[0-9]/

    %import common.WS
    %ignore WS
"""

# Ejemplo de entrada válida
chef_code = """
Hey.

Ingredients.
121 g y
101 ml e
72 cup h

Method.
Put y into the mixing bowl.
Put e into the mixing bowl.
Put h into the mixing bowl.
Liquefy contents of the mixing bowl.
Pour contents of the mixing bowl into the baking dish.

Serves 1.
"""


parser = Lark(chef_grammar, start="start", parser="lalr")
tree = parser.parse(chef_code)

pydot__tree_to_png(tree, "src/arbol.png")