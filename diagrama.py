import sys
import pathlib
from railroad import Diagram, Stack, Choice, HorizontalChoice, Sequence, Terminal, NonTerminal, OneOrMore, Optional, ZeroOrMore


prog = Diagram(
  Stack(
    Sequence(NonTerminal("Identificador"), Terminal(".")), Sequence(Terminal("Ingredients ."), NonTerminal("ListaIngredientes")), Sequence(Terminal("Methods ."), NonTerminal("Metodos")), 
    Optional(
      Sequence(
        Terminal("Serves"), NonTerminal("Entero"), Terminal(".")
      )
    )
  )
)
ingredientes = Diagram(
  Sequence(OneOrMore(NonTerminal("Ingrediente")))
)
ingrediente = Diagram(
  Sequence(
    NonTerminal("Entero"), Optional(NonTerminal("Unidad")), NonTerminal("Identificador")
  )
)

unidad = Diagram(Sequence(Choice(0, NonTerminal("Seco"), Sequence(Optional(NonTerminal("Modificador")), Choice(0, NonTerminal("Liquido"), NonTerminal("Volumen"))))
))

modificador = Diagram(Sequence(Choice(0, Terminal("heaped"), Terminal("level"))))

seco = Diagram(Sequence(Choice(1, Terminal("g"), Terminal("kg"), Terminal("pinch"))))

liquido = Diagram(Sequence(Choice(0, Terminal("ml"), Terminal("l"))))

volumen = Diagram(Sequence(Choice(1, Terminal("tablespoon"), Terminal("teaspoon"), Terminal("cup"))))

metodos = Diagram(OneOrMore(NonTerminal("Instruccion")))

instruccion = Diagram(
Sequence(
Choice(
0, 
NonTerminal("InstruccionAIngrediente"),
Sequence(Terminal("Add dry ingredients"), Optional(Sequence(Terminal("to"), NonTerminal("RecipienteMezcla")))),
Sequence(Terminal("Liquefy"), Choice(0, Sequence(Terminal("contents of"), NonTerminal("RecipienteMezcla")), NonTerminal("Identificador"))),
Sequence(Terminal("Stir"), Choice(0, Sequence(Optional(NonTerminal("RecipienteMezcla")), Terminal("for"), NonTerminal("Entero"), Terminal("minutes")), Sequence(NonTerminal("Identificador"), Terminal("into"), NonTerminal("RecipienteMezcla")))),
Sequence(Terminal("Mix"), Optional(NonTerminal("RecipienteMezcla")), Terminal("well")),
Sequence(Terminal("Clean"), NonTerminal("RecipienteMezcla")),
Sequence(Terminal("Pour contents of"), NonTerminal("RecipienteMezcla"), Terminal("into"), NonTerminal("RecipienteHorneado")),
Sequence(Terminal("Serve with"), NonTerminal("Identificador"))
)
), 
Terminal(".")
)

instruccionAIngrediente = Diagram(Choice(0,
Sequence(Choice(0, Terminal("Put"), Terminal("Fold")), NonTerminal("Identificador"), Terminal("into"), NonTerminal("RecipienteMezcla")),
Sequence(Terminal("Remove"), NonTerminal("Identificador"), Optional(Sequence(Terminal("from"), NonTerminal("RecipienteMezcla")))),
Sequence(
Choice(
0,
Sequence(Choice(0, Terminal("Add"), Terminal("Combine"), Terminal("Divide")), NonTerminal("Identificador"), Optional(Sequence(Terminal("into"), NonTerminal("RecipienteMezcla"))))))))

recipienteMezcla = Diagram(Sequence(Optional(Terminal("the")), Optional(NonTerminal("Ordinal")), Terminal("mixing bowl")))

recipienteHorneado = Diagram(Sequence(Optional(Terminal("the")), Optional(NonTerminal("Ordinal")), Terminal("baking dish")))

ordinal = Diagram(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"), Terminal("6th"), Terminal("7th"), Terminal("8th"), Terminal("9th"), Terminal("10th")))
entero = Diagram(OneOrMore(NonTerminal("Digito")))
identificador = Diagram(OneOrMore(Choice(0, NonTerminal("Letra"), NonTerminal("Digito"))))
letra = Diagram(OneOrMore(HorizontalChoice(Terminal("A"), Terminal("B"), Terminal("C"), Terminal("..."), Terminal("Z"), Terminal("a"), Terminal("b"), Terminal("c"), Terminal("..."), Terminal("z"))))
digito = Diagram(OneOrMore(HorizontalChoice(Terminal("0"), Terminal("1"), Terminal("2"), Terminal("3"), Terminal("4"), Terminal("5"), Terminal("6"), Terminal("7"), Terminal("8"), Terminal("9"))))

programa_path = pathlib.Path("src/programa.svg")
with programa_path.open("w", encoding="utf-8") as f:
    prog.writeStandalone(f.write)

ingrediente_path = pathlib.Path("src/ingrediente.svg")
with ingrediente_path.open("w", encoding="utf-8") as f:
    ingrediente.writeStandalone(f.write)

ingredientes_path = pathlib.Path("src/listaIngredientes.svg")
with ingredientes_path.open("w", encoding="utf-8") as f:
    ingredientes.writeStandalone(f.write)
  
unidad_path = pathlib.Path("src/unidad.svg")
with unidad_path.open("w", encoding="utf-8") as f:
    unidad.writeStandalone(f.write)

modificador_path = pathlib.Path("src/modificador.svg")
with modificador_path.open("w", encoding="utf-8") as f:
    modificador.writeStandalone(f.write)

seco_path = pathlib.Path("src/seco.svg")
with seco_path.open("w", encoding="utf-8") as f:
    seco.writeStandalone(f.write)

liquido_path = pathlib.Path("src/liquido.svg")
with liquido_path.open("w", encoding="utf-8") as f:
    liquido.writeStandalone(f.write)

volumen_path = pathlib.Path("src/volumen.svg")
with volumen_path.open("w", encoding="utf-8") as f:
    volumen.writeStandalone(f.write)

metodos_path = pathlib.Path("src/metodos.svg")
with metodos_path.open("w", encoding="utf-8") as f:
    metodos.writeStandalone(f.write)

instruccion_path = pathlib.Path("src/instruccion.svg")
with instruccion_path.open("w", encoding="utf-8") as f:
    instruccion.writeStandalone(f.write)

instruccionAIngrediente_path = pathlib.Path("src/instruccionAIngrediente.svg")
with instruccionAIngrediente_path.open("w", encoding="utf-8") as f:
    instruccionAIngrediente.writeStandalone(f.write)

recipienteMezcla_path = pathlib.Path("src/recipienteMezcla.svg")
with recipienteMezcla_path.open("w", encoding="utf-8") as f:
    recipienteMezcla.writeStandalone(f.write)


recipienteHorneado_path = pathlib.Path("src/recipienteHorneado.svg")
with recipienteHorneado_path.open("w", encoding="utf-8") as f:
    recipienteHorneado.writeStandalone(f.write)

ordinal_path = pathlib.Path("src/ordinal.svg")
with ordinal_path.open("w", encoding="utf-8") as f:
    ordinal.writeStandalone(f.write)

entero_path = pathlib.Path("src/entero.svg")
with entero_path.open("w", encoding="utf-8") as f:
    entero.writeStandalone(f.write)

identificador_path = pathlib.Path("src/identificador.svg")
with identificador_path.open("w", encoding="utf-8") as f:
    identificador.writeStandalone(f.write)

letra_path = pathlib.Path("src/letra.svg")
with letra_path.open("w", encoding="utf-8") as f:
    letra.writeStandalone(f.write)

digito_path = pathlib.Path("src/digito.svg")
with digito_path.open("w", encoding="utf-8") as f:
    digito.writeStandalone(f.write)