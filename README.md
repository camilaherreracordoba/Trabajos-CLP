# Caracteristicas de los lenguajes de programación

Chef es un lenguaje esoterico basado en pilas. Tiene la particularidad de que los programas se asemejan a recetas de cocina. 

### GIC

```text
Programa -> NombreReceta . Ingredients. Ingredientes Method. Metodo 
          | NombreReceta . Ingredients. Ingrediente Method. Metodo Serves Entero .

NombreReceta -> Palabra NombreReceta | Palabra

NombreIngrediente -> Palabra NombreIngrediente | Palabra

Ingredientes -> Ingrediente Ingredientes | Ingrediente 
Ingrediente -> Entero Unidad NombreIngrediente 
             | Entero NombreIngrediente 

Unidad -> Seco | Liquido | Volumen 
        | Modificador Liquido
        | Modificador Volumen

Seco -> g | kg | pinch

Liquido -> ml | l 

Volumen -> tablespoon | teaspoon | cup

Modificador -> heaped | level

Metodo -> Instruccion | Instruccion Metodo

Instruccion -> Add NombreIngrediente into RecipienteMezcla . | Add NombreIngrediente .
             | Put NombreIngrediente into RecipienteMezcla .
             | Fold NombreIngrediente into RecipienteMezcla .
             | Remove NombreIngrediente from RecipienteMezcla . | Remove NombreIngrediente .
             | Combine NombreIngrediente into RecipienteMezcla . | Combine NombreIngrediente .
             | Divide NombreIngrediente into RecipienteMezcla . | Divide NombreIngrediente .
             | Add dry ingredients to RecipienteMezcla . | Add dry ingredients .
             | Liquefy contents of RecipienteMezcla . | Liquefy NombreIngrediente .
             | Stir the RecipienteMezcla for Entero minutes . | Stir for Entero minutes . | Stir NombreIngrediente into RecipienteMezcla . 
             | Mix RecipienteMezcla well . | Mix well . 
             | Clean RecipienteMezcla .
             | Pour contents of RecipienteMezcla into RecipienteHorneado . 
             | Serve with NombreReceta . 

RecipienteMezcla -> mixing bowl | the mixing bowl | Ordinal mixing bowl | the Ordinal mixing bowl
RecipienteHorneado -> baking dish | the baking dish | Ordinal baking dish | the Ordinal baking dish

Ordinal -> 1st | 2nd | 3rd | 4th | ...
Palabra -> Letra Palabra | Numero Palabra | Letra | Numero 
Letra -> A | B | C | ... | a | b | c | ...
Entero -> Numero Entero | Numero
Numero -> 0 |1 | 2 | 3 | ...

```
### BNF
```bnf
<Programa> ::= <NombreReceta> "." "Ingredients." <Ingredientes> <Metodo>
            | <NombreReceta> "." "Ingredients." <Ingrediente> <Metodo> "Serves" <Entero> "."

<NombreReceta> ::= <Palabra> <NombreReceta> | <Palabra>

<NombreIngrediente> ::= <Palabra> <NombreIngrediente> | <Palabra>

<Ingredientes> ::= <Ingrediente> <Ingredientes> | <Ingrediente>

<Ingrediente> ::= <Entero> <Unidad> <NombreIngrediente>
              | <Entero> <NombreIngrediente>

<Unidad> ::= <Seco> | <Liquido> | <Volumen> | <Modificador> <Liquido> | <Modificador> <Volumen>

<Seco> ::= "g" | "kg" | "pinch"

<Liquido> ::= "ml" | "l"

<Volumen> ::= "tablespoon" | "teaspoon" | "cup"

<Modificador> ::= "heaped" | "level"

<Metodo> ::= <Instruccion> | <Instruccion> <Metodo>

<Instruccion> ::= "Add" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Add" <NombreIngrediente> "."
              | "Put" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Fold" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Remove" <NombreIngrediente> "from" <RecipienteMezcla> "."
              | "Remove" <NombreIngrediente> "."
              | "Combine" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Combine" <NombreIngrediente> "."
              | "Divide" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Divide" <NombreIngrediente> "."
              | "Add dry ingredients" "to" <RecipienteMezcla> "."
              | "Add dry ingredients" "."
              | "Liquefy contents of" <RecipienteMezcla> "."
              | "Liquefy" <NombreIngrediente> "."
              | "Stir" "the" <RecipienteMezcla> "for" <Entero> "minutes" "."
              | "Stir" "for" <Entero> "minutes" "."
              | "Stir" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Mix" <RecipienteMezcla> "well" "."
              | "Mix" "well" "."
              | "Clean" <RecipienteMezcla> "."
              | "Pour contents of" <RecipienteMezcla> "into" <RecipienteHorneado> "."
              | "Serve with" <NombreReceta> "."

<RecipienteMezcla> ::= "mixing bowl" | "the mixing bowl" | "the" <Ordinal> "mixing bowl" | <Ordinal> "mixing bowl"

<RecipienteHorneado> ::= "baking dish" | "the baking dish" | <Ordinal> "baking dish" | "the" <Ordinal> "baking dish"
<Ordinal> ::= "1st" | "2nd" | "3rd" | "4th" | ...

<Palabra> ::= <Letra> <Palabra> | <Numero> <Palabra> | <Letra> | <Numero>

<Letra> ::= "A" | "B" | "C" | ... | "a" | "b" | "c" | ...

<Entero> -> <Numero> <Entero> | <Numero>

<Numero> ::= "0" | "1" | "2" | "3" | ...
```

### EBNF
```ebnf
Programa ::= NombreReceta "." "Ingredients." Ingredientes Metodo
            | NombreReceta "." "Ingredients." Ingrediente Metodo "Serves" Entero "."

NombreReceta ::= {Palabra}+
NombreIngrediente ::= {Palabra}+
Ingredientes ::= {Ingrediente}+

Ingrediente ::= Entero [Unidad] NombreIngrediente
Unidad ::= Seco | [Modificador] Liquido | [Modificador] Volumen

Modificador ::= "heaped" | "level"
Seco ::= "g" | "kg" | "pinch"

Liquido ::= "ml" | "l"

Volumen ::= "tablespoon" | "teaspoon" | "cup"

Metodo ::= {Instruccion}+

Instruccion ::= "Add" NombreIngrediente ["into" RecipienteMezcla] "." 
             | "Put" NombreIngrediente "into" RecipienteMezcla "."
             | "Fold" NombreIngrediente "into" RecipienteMezcla "."
             | "Remove" NombreIngrediente ["from" RecipienteMezcla] "." 
             | "Combine" NombreIngrediente ["into" RecipienteMezcla] "." 
             | "Divide" NombreIngrediente ["into" RecipienteMezcla] "."
             | "Add dry ingredients" ["to" RecipienteMezcla] "." 
             | "Liquefy" ("contents of" RecipienteMezcla | NombreIngrediente) "." 
             | "Stir" ([RecipienteMezcla] "for" Entero "minutes" | NombreIngrediente "into" RecipienteMezcla) "." 
             | "Mix" [RecipienteMezcla] "well" . 
             | "Clean" RecipienteMezcla "."
             | "Pour contents of" RecipienteMezcla "into" RecipienteHorneado "." 
             | "Serve with" NombreReceta "." 

RecipienteMezcla ::= ["the"] [Ordinal] "mixing bowl"
RecipienteHorneado ::= ["the"] [Ordinal] "baking dish" .

Ordinal ::= "1st" | "2nd" | "3rd" | "4th" | "5th" | ...

Palabra ::= {Letra | Numero}+

Entero ::= {Numero}+ 

Letra ::= A | B | C | ... | a | b | c | ... | z

Numero ::= 0 | ... | 9
```
### ABNF
```abnf
Programa = NombreReceta "." "Ingredients." Ingredientes Metodo
         / NombreReceta "." "Ingredients." Ingrediente Metodo "Serves" Entero "."

NombreReceta = 1*(Palabra)
NombreIngrediente = 1*(Palabra)

Ingredientes = 1*(Ingrediente)

Ingrediente = Entero [Unidad] NombreIngrediente

Unidad = Seco
       / [Modificador] Liquido
       / [Modificador] Volumen

Modificador = "heaped" / "level"
Seco = "g" / "kg" / "pinch"
Liquido = "ml" / "l"
Volumen = "tablespoon" / "teaspoon" / "cup"

Metodo = 1*(Instruccion)

Instruccion = "Add" NombreIngrediente ["into" RecipienteMezcla] "."
            / "Put" NombreIngrediente "into" RecipienteMezcla "."
            / "Fold" NombreIngrediente "into" RecipienteMezcla "."
            / "Remove" NombreIngrediente ["from" RecipienteMezcla] "."
            / "Combine" NombreIngrediente ["into" RecipienteMezcla] "."
            / "Divide" NombreIngrediente ["into" RecipienteMezcla] "."
            / "Add dry ingredients" ["to" RecipienteMezcla] "."
            / "Liquefy" ("contents of" RecipienteMezcla / NombreIngrediente) "."
            / "Stir" ((RecipienteMezcla "for" Entero "minutes") / ("for" Entero "minutes") / (NombreIngrediente "into" RecipienteMezcla)) "."
            / "Mix" [RecipienteMezcla] "well" "."
            / "Clean" RecipienteMezcla "."
            / "Pour contents of" RecipienteMezcla "into" RecipienteHorneado "."
            / "Serve with" NombreReceta "."

RecipienteMezcla = ["the"] [Ordinal] "mixing bowl"
RecipienteHorneado = ["the"] [Ordinal] "baking dish"

Ordinal = "1st" / "2nd" / "3rd" / "4th" / "5th" / ...

Palabra = 1*(Letra / Numero)
Entero = 1*(Numero)
Letra = %x41-5A / %x61-7A 
Numero = %x30-39 


```


![Ver diagrama SVG](diagrama.svg)
