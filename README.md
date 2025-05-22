# Caracteristicas de los lenguajes de programación

Chef es un lenguaje esoterico basado en pilas. Tiene la particularidad de que los programas se asemejan a recetas de cocina. 

### GIC

```text
Programa -> Identificador . Ingredients. ListaIngredientes Method. Metodos 
          | Identificador . Ingredients. Ingrediente Method. Metodos Serves Entero .

ListaIngredientes -> Ingrediente ListaIngredientes | Ingrediente 
Ingrediente -> Entero Unidad Identificador 
             | Entero Identificador 

Unidad -> Seco | Liquido | Volumen 
        | Modificador Liquido
        | Modificador Volumen

Seco -> g | kg | pinch

Liquido -> ml | l 

Volumen -> tablespoon | teaspoon | cup

Modificador -> heaped | level

Metodos -> Instruccion | Instruccion Metodos

Instruccion -> InstruccionAIngrediente .
             | Add dry ingredients to RecipienteMezcla . | Add dry ingredients .
             | Liquefy contents of RecipienteMezcla . | Liquefy Identificador .
             | Stir the RecipienteMezcla for Entero minutes . | Stir for Entero minutes . | Stir Identificador into RecipienteMezcla . 
             | Mix RecipienteMezcla well . | Mix well . 
             | Clean RecipienteMezcla .
             | Pour contents of RecipienteMezcla into RecipienteHorneado . 
             | Serve with Identificador . 

InstruccionAIngrediente -> Add Identificador into RecipienteMezcla
                | Add Identificador
                | Combine Identificador into RecipienteMezcla
                | Combine Identificador
                | Divide Identificador into RecipienteMezcla
                | Divide Identificador
                | Put Identificador into RecipienteMezcla
                | Fold Identificador into RecipienteMezcla
                | Remove Identificador from RecipienteMezcla
                | Remove Identificador

RecipienteMezcla -> mixing bowl | the mixing bowl | Ordinal mixing bowl | the Ordinal mixing bowl
RecipienteHorneado -> baking dish | the baking dish | Ordinal baking dish | the Ordinal baking dish

Ordinal -> 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th

Identificador -> Letra Identificador
               | Numero Identificador
               | Letra
               | Numero

Letra -> A | B | C | ... | a | b | c | ...
Entero -> Numero Entero | Numero
Numero -> 0 |1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 

```
### BNF
```bnf
<Programa> ::= <Identificador> "." "Ingredients." <ListaIngredientes> <Metodos>
            | <Identificador> "." "Ingredients." <Ingrediente> <Metodos> "Serves" <Entero> "."


<ListaIngredientes> ::= <Ingrediente> <ListaIngredientes> | <Ingrediente>

<Ingrediente> ::= <Entero> <Unidad> <Identificador>
              | <Entero> <Identificador>

<Unidad> ::= <Seco> | <Liquido> | <Volumen> | <Modificador> <Liquido> | <Modificador> <Volumen>

<Seco> ::= "g" | "kg" | "pinch"

<Liquido> ::= "ml" | "l"

<Volumen> ::= "tablespoon" | "teaspoon" | "cup"

<Modificador> ::= "heaped" | "level"

<Metodos> ::= <Instruccion> | <Instruccion> <Metodos>

<Instruccion> ::= <InstruccionAIngrediente> "."
                | "Add dry ingredients" "to" <RecipienteMezcla> "."
                | "Add dry ingredients" "."
                | "Liquefy contents of" <RecipienteMezcla> "."
                | "Liquefy" <Identificador> "."
                | "Stir" "the" <RecipienteMezcla> "for" <Entero> "minutes" "."
                | "Stir" "for" <Entero> "minutes" "."
                | "Stir" <Identificador> "into" <RecipienteMezcla> "."
                | "Mix" <RecipienteMezcla> "well" "."
                | "Mix" "well" "."
                | "Clean" <RecipienteMezcla> "."
                | "Pour contents of" <RecipienteMezcla> "into" <RecipienteHorneado> "."
                | "Serve with" <Identificador> "."

<InstruccionAIngrediente> ::= "Add" <Identificador> "into" <RecipienteMezcla>
                             | "Add" <Identificador>
                             | "Combine" <Identificador> "into" <RecipienteMezcla>
                             | "Combine" <Identificador>
                             | "Divide" <Identificador> "into" <RecipienteMezcla>
                             | "Divide" <Identificador>
                             | "Put" <Identificador> "into" <RecipienteMezcla>
                             | "Fold" <Identificador> "into" <RecipienteMezcla>
                             | "Remove" <Identificador> "from" <RecipienteMezcla>
                             | "Remove" <Identificador>

<RecipienteMezcla> ::= "mixing bowl" | "the mixing bowl" | "the" <Ordinal> "mixing bowl" | <Ordinal> "mixing bowl"

<RecipienteHorneado> ::= "baking dish" | "the baking dish" | <Ordinal> "baking dish" | "the" <Ordinal> "baking dish"

<Ordinal> ::= "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th"

<Identificador> ::= <Letra> <Identificador> 
                | <Numero> <Identificador> 
                | <Letra> 
                | <Numero>

<Letra> ::= "A" | "B" | "C" | ... | "a" | "b" | "c" | ...

<Entero> ::= <Numero> <Entero> | <Numero>

<Numero> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

### EBNF
```ebnf
Programa ::= Identificador "." "Ingredients." ListaIngredientes Metodos
            | Identificador "." "Ingredients." Ingrediente Metodos "Serves" Entero "."

ListaIngredientes ::= {Ingrediente}+

Ingrediente ::= Entero [Unidad] Identificador
Unidad ::= Seco | [Modificador] Liquido | [Modificador] Volumen

Modificador ::= "heaped" | "level"
Seco ::= "g" | "kg" | "pinch"

Liquido ::= "ml" | "l"

Volumen ::= "tablespoon" | "teaspoon" | "cup"

Metodos ::= {Instruccion}+

Instruccion ::= (InstruccionAIngrediente
             | "Add dry ingredients" ["to" RecipienteMezcla] 
             | "Liquefy" ("contents of" RecipienteMezcla | Identificador) 
             | "Stir" ([RecipienteMezcla] "for" Entero "minutes" | Identificador "into" RecipienteMezcla) 
             | "Mix" [RecipienteMezcla] "well"
             | "Clean" RecipienteMezcla
             | "Pour contents of" RecipienteMezcla "into" RecipienteHorneado 
             | "Serve with" Identificador) "." 

InstruccionAIngrediente ::= ( ("Put" | "Fold") Identificador "into" RecipienteMezcla 
            | "Remove" Identificador [ "from" RecipienteMezcla ] 
            | ("Add" | "Combine" | "Divide") Identificador [ "into" RecipienteMezcla ])

RecipienteMezcla ::= ["the"] [Ordinal] "mixing bowl"
RecipienteHorneado ::= ["the"] [Ordinal] "baking dish"

Ordinal ::= "1st" | "2nd" | "3rd" | "4th" | "5th" | "6th" | "7th" | "8th" | "9th" | "10th"

Identificador ::= {Letra | Numero}+

Entero ::= {Numero}+ 

Letra ::= "A" | "B" | "C" | ...  | "Z" | "a" | "b" | "c" | ... | "z"

Numero ::= "0" | ... | "9"
```
### ABNF
```abnf
Programa = Identificador "." "Ingredients." ListaIngredientes Metodos
         / Identificador "." "Ingredients." Ingrediente Metodos "Serves" Entero "."


ListaIngredientes = 1*(Ingrediente)

Ingrediente = Entero [Unidad] Identificador

Unidad = Seco
       / [Modificador] (Liquido / Volumen)

Modificador = "heaped" / "level"
Seco = "g" / "kg" / "pinch"
Liquido = "ml" / "l"
Volumen = "tablespoon" / "teaspoon" / "cup"

Metodos = 1*(Instruccion)

Instruccion = (InstruccionAIngrediente
            / "Add dry ingredients" ["to" RecipienteMezcla] 
            / "Liquefy" ("contents of" RecipienteMezcla / Identificador) 
            / "Stir" ((RecipienteMezcla "for" Entero "minutes") / ("for" Entero "minutes") / (Identificador "into" RecipienteMezcla)) 
            / "Mix" [RecipienteMezcla] "well" 
            / "Clean" RecipienteMezcla 
            / "Pour contents of" RecipienteMezcla "into" RecipienteHorneado 
            / "Serve with" Identificador) "."

InstruccionAIngrediente = ( ("Put" / "Fold") Identificador "into" RecipienteMezcla 
            / "Remove" Identificador [ "from" RecipienteMezcla ] 
            / ("Add" / "Combine" / "Divide") Identificador [ "into" RecipienteMezcla ])
RecipienteMezcla = ["the"] [Ordinal] "mixing bowl"
RecipienteHorneado = ["the"] [Ordinal] "baking dish"

Ordinal = "1st" / "2nd" / "3rd" / "4th" / "5th" / "6th" / "7th" / "8th" / "9th" / "10th"

Identificador = 1*(Letra / Numero)
Entero = 1*(Numero)
Letra = %x41-5A / %x61-7A 
Numero = %x30-39 


```

## Diagrama de sintaxis

### Programa
![Ver diagrama programa SVG](src/programa.svg)
## Lista ingredientes
![diagrama ingredientes](src/listaIngredientes.svg)
### Ingrediente
![Ver diagrama ingrediente](src/ingrediente.svg)
### Unidad
![Diagrama Unidad](src/unidad.svg)
#### Modificador
![Diagrama Modificador](src/modificador.svg)
#### Seco
![Diagrama Seco](src/seco.svg)
#### Liquido
![Diagrama Liquido](src/liquido.svg)
#### Volumen
![Diagrama Volumen](src/volumen.svg)

## Metodos
![Diagrama metodos](src/metodos.svg)
### Instruccion
![Diagrama instrucciones](src/instruccion.svg)
### Instruccion a ingredientes
![Diagrama instruccion sobre ingredientes](src/instruccionSobreIngrediente.svg)
### Recipiente mezcla
![Diagrama recipiente mezcla](src/recipienteMezcla.svg)
### Recipiente horneado
![Diagrama recipiente horneado](src/recipienteHorneado.svg)


### Ordinal
![diagrama ordinal](src/ordinal.svg)
### Entero
![diagrama entero](src/entero.svg)
### Identificador
![diagrama identificador](src/identificador.svg)
### Letra
![diagrama letra](src/letra.svg)
### Digito
![diagrama digito](src/digito.svg)