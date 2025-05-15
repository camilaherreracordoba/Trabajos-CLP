# Caracteristicas de los lenguajes de programación

Chef es un lenguaje esoterico basado en pilas. Tiene la particularidad de que los programas se asemejan a recetas de cocina. 

### GIC

```
Programa -> NombreReceta . Ingredients. Ingredientes Method. Metodo 
          | NombreReceta . Ingredients. Ingrediente Method. Metodo Serves Numero .

NombreReceta -> Palabra NombreReceta | Palabra

NombreIngrediente -> Palabra NombreIngrediente | Palabra

Ingredientes -> Ingrediente Ingredientes | Ingrediente 
Ingrediente -> Numero Unidad NombreIngrediente 
             | Numero NombreIngrediente 

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
             | Stir the RecipienteMezcla for Numero minutes . | Stir for Numero minutes . | Stir NombreIngrediente into RecipienteMezcla . 
             | Mix RecipienteMezcla well . | Mix well . 
             | Clean RecipienteMezcla .
             | Pour contents of RecipienteMezcla into the Ordinal baking dish . 
             | Serve with NombreReceta . 

RecipienteMezcla -> mixing bowl | Ordinal mixing bowl | the Ordinal mixing bowl

Ordinal -> 1st | 2nd | 3rd | 4th | ...
Palabra -> Letra Palabra | Numero Palabra | Letra | Numero 
Letra -> A | B | C | ... | a | b | c | ...
Numero -> 0 |1 | 2 | 3 | ...

```
### BNF
```haskell
<Programa> ::= <NombreReceta> "." "Ingredients." <Ingredientes> <Metodo>
            | <NombreReceta> "." "Ingredients." <Ingrediente> <Metodo> "Serves" <Numero> "."

<NombreReceta> ::= <Palabra> <NombreReceta> | <Palabra>

<NombreIngrediente> ::= <Palabra> <NombreIngrediente> | <Palabra>

<Ingredientes> ::= <Ingrediente> <Ingredientes> | <Ingrediente>

<Ingrediente> ::= <Numero> <Unidad> <NombreIngrediente>
              | <Numero> <NombreIngrediente>

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
              | "Stir" "the" <RecipienteMezcla> "for" <Numero> "minutes" "."
              | "Stir" "for" <Numero> "minutes" "."
              | "Stir" <NombreIngrediente> "into" <RecipienteMezcla> "."
              | "Mix" <RecipienteMezcla> "well" "."
              | "Mix" "well" "."
              | "Clean" <RecipienteMezcla> "."
              | "Pour contents of" <RecipienteMezcla> "into" "the" <Ordinal> "baking dish" "."
              | "Serve with" <NombreReceta> "."

<RecipienteMezcla> ::= "mixing bowl" | "the" <Ordinal> "mixing bowl" | <Ordinal> "mixing bowl"

<Ordinal> ::= λ | "1st" | "2nd" | "3rd" | "4th" | ...

<Palabra> ::= <Letra> <Palabra> | <Numero> <Palabra> | <Letra> | <Numero>

<Letra> ::= "A" | "B" | "C" | ... | "a" | "b" | "c" | ...

<Numero> ::= "0" | "1" | "2" | "3" | ...
```
