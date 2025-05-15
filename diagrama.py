import sys
from railroad import Diagram, Choice, Sequence, Terminal, NonTerminal, OneOrMore, Optional
# Definir un estilo personalizado para el diagrama
css = """
    svg.railroad-diagram {
        background-color: white;
    }
    svg.railroad-diagram path {
        stroke-width: 2;
        stroke: black;
    }
    svg.railroad-diagram text {
        font-family: sans-serif;
        font-size: 14px;
        fill: black;
    }
    svg.railroad-diagram rect {
        fill: #DCEDC8; /* Fondo verde claro para los recuadros */
    }
    svg.railroad-diagram rect.terminal {
        fill: #B3E5FC; /* Fondo azul claro para terminales */
        stroke: black;
    }
    svg.railroad-diagram rect.non-terminal {
        fill: #FFECB3; /* Fondo amarillo claro para no terminales */
        stroke: black;
    }
    svg.railroad-diagram rect.choice {
        fill: #E1BEE7; /* Fondo púrpura claro para opciones */
    }
"""
d = Diagram(
  Choice(0,
    Sequence(
      OneOrMore(NonTerminal("Palabra")), ".",
      Terminal("Ingredients."),
      OneOrMore(
        Sequence(
          NonTerminal("Entero"),
          Optional(
            Choice(0,
              Terminal("g"),
              Terminal("kg"),
              Terminal("pinch"),
              Sequence(
                Optional(Choice(0, Terminal("heaped"), Terminal("level"))),
                Choice(0, Terminal("ml"), Terminal("l"))
              ),
              Sequence(
                Optional(Choice(0, Terminal("heaped"), Terminal("level"))),
                Choice(0, Terminal("tablespoon"), Terminal("teaspoon"), Terminal("cup"))
              )
            )
          ),
          OneOrMore(NonTerminal("Palabra"))
        )
      ),
      OneOrMore(
        Choice(0,
          Sequence("Add", OneOrMore(NonTerminal("Palabra")),
            Optional(Sequence("into",
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl"))),
            "."
          ),
          Sequence("Put", OneOrMore(NonTerminal("Palabra")),
            "into",
            Optional("the"),
            Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
            Terminal("mixing bowl"),
            "."
          ),
          Sequence("Fold", OneOrMore(NonTerminal("Palabra")),
            "into",
            Optional("the"),
            Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
            Terminal("mixing bowl"),
            "."
          ),
          Sequence("Remove", OneOrMore(NonTerminal("Palabra")),
            Optional(Sequence("from",
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl"))),
            "."
          ),
          Sequence("Combine", OneOrMore(NonTerminal("Palabra")),
            Optional(Sequence("into",
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl"))),
            "."
          ),
          Sequence("Divide", OneOrMore(NonTerminal("Palabra")),
            Optional(Sequence("into",
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl"))),
            "."
          ),
          Sequence("Add dry ingredients",
            Optional(Sequence("to",
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl"))),
            "."
          ),
          Sequence("Liquefy",
            Choice(0,
              Sequence("contents of",
                Optional("the"),
                Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
                Terminal("mixing bowl")),
              OneOrMore(NonTerminal("Palabra"))
            ),
            "."
          ),
          Sequence("Stir",
            Choice(0,
              Sequence(
                Optional("the"),
                Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
                Terminal("mixing bowl"),
                "for",
                OneOrMore(NonTerminal("Numero")),
                "minutes"
              ),
              Sequence("for", OneOrMore(NonTerminal("Numero")), "minutes"),
              Sequence(OneOrMore(NonTerminal("Palabra")), "into",
                Optional("the"),
                Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
                Terminal("mixing bowl"))
            ),
            "."
          ),
          Sequence("Mix",
            Optional(Sequence(
              Optional("the"),
              Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
              Terminal("mixing bowl")
            )),
            "well",
            "."
          ),
          Sequence("Clean",
            Optional("the"),
            Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
            Terminal("mixing bowl"),
            "."
          ),
          Sequence("Pour contents of",
            Optional("the"),
            Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
            Terminal("mixing bowl"),
            "into",
            Optional("the"),
            Optional(Choice(0, Terminal("1st"), Terminal("2nd"), Terminal("3rd"), Terminal("4th"), Terminal("5th"))),
            Terminal("baking dish"),
            "."
          ),
          Sequence("Serve with", OneOrMore(NonTerminal("Palabra")), ".")
        )
      )
    ),
    Sequence(
      OneOrMore(NonTerminal("Palabra")), ".",
      Terminal("Ingredients."),
      Sequence(
        NonTerminal("Entero"),
        Optional(
          Choice(0,
            Terminal("g"),
            Terminal("kg"),
            Terminal("pinch"),
            Sequence(
              Optional(Choice(0, Terminal("heaped"), Terminal("level"))),
              Choice(0, Terminal("ml"), Terminal("l"))
            ),
            Sequence(
              Optional(Choice(0, Terminal("heaped"), Terminal("level"))),
              Choice(0, Terminal("tablespoon"), Terminal("teaspoon"), Terminal("cup"))
            )
          )
        ),
        OneOrMore(NonTerminal("Palabra"))
      ),
      OneOrMore(NonTerminal("Instruccion")),
      Terminal("Serves"),
      OneOrMore(NonTerminal("Numero")),
      "."
    )
  ),
  css=css

)

with open("diagrama.svg", "w", encoding="utf-8") as f:
    d.writeSvg(f.write)

print("'diagrama.svg'")