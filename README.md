# Caracteristicas de los lenguajes de programación
## TP 1
[Mapa conceptual](https://www.mermaidchart.com/raw/30bd0048-315a-4ec0-bd83-ce62b3d13edc?theme=light&version=v0.1&format=svg)
## TP 2

[Clasificacion de lenguajes](https://docs.google.com/spreadsheets/d/19aTSzIjQNs6RBNJFz0bftTlqKr-uWbohbBZnxmP0-r0/edit?gid=0#gid=0)

## TP 3
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
<Programa> ::= <Identificador> "." "Ingredients." <ListaIngredientes> "Methods." <Metodos>
            | <Identificador> "." "Ingredients." <Ingrediente> "Methods." <Metodos> "Serves" <Entero> "."


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
Programa ::= Identificador "." "Ingredients." ListaIngredientes "Method." Metodos
            | Identificador "." "Ingredients." Ingrediente "Method" Metodos "Serves" Entero "."

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
Programa = Identificador "." "Ingredients." ListaIngredientes "Method."Metodos
         / Identificador "." "Ingredients." Ingrediente "Method." Metodos "Serves" Entero "."


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
### TP 4
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

## Arbol sintactico:

```
Hey.

Ingredients.

72 cup h

Method.
Put h into the mixing bowl.
Liquefy contents of the mixing bowl.
Pour contents of the mixing bowl into the baking dish.

Serves 1.
```
> Output: H

[diagrama arbol](src/arbol.png)

## TP 5

| Binding | Estático | Dinámico | Ejemplo estático | Ejemplo dinámico |
| -- | -- | -- | -- | -- |
| **De valor**   | Ninguno, en el momento de la compilación no se pueden predecir los valores | Casi todos los lenguajes | - | func(x+1, 2) |
| **De tipo**    | El tipo se define explicitamente: C, C++, Java | El tipo se puede inferir: Python, Javascript | void func(int entero, string palabra) <br> {...} // C, C++  | def func(entero, palabra): <br> ... |
| **De alcance** | C, C++, Java, Python, JavaScript, Rust, Pascal, Haskell, etc. tienen alcance dentro del cuerpo de la funcion | En algunos lenguajes se pueden usar closures o en lenguajes con expresiones como eval y global (Python) | ... | - |
| **De almacenamiento** | En stack de forma fija | En heap, pero también puede capturarse con closure | - | - |
| **De nombre**         | El nombre del parámetro es fijo en la definición (C, C++, Java, Pascal, Javascript) | Se pueden usar tecnicas para crear nombres dinámicos (**kwargs, reflexión, eval) |  void saludar(char* nombre) {print ("Hola, %s\n", nombre);} <br> int main() { saludar("Pablo"); return 0; } | def funcion(**kwargs): <br> for nombre, valor in kwargs.items(): <br> print(f"{nombre}: {valor}") |
|**De tiempo de vida**| Los parámetros "viven" durante el tiempo de ejecucion de la funcion | Puede tenerse un tiempo de vida extendido en caso de usar closures | void func(x) {return x + 1;} // x no existe luego de usar la funcion | - |


### TP Final
[Trabajo practico final](parcial.md)

