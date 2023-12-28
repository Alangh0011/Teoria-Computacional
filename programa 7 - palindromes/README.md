# Práctica de Teoría Computacional - Programa 7: Palíndromos Binarios

## Descripción

Este programa construye palíndromos binarios de acuerdo con una gramática libre de contexto dada. El usuario puede especificar la longitud del palíndromo o generar uno automáticamente.

## Gramática Libre de Contexto

La gramática libre de contexto que construye palíndromos es la siguiente:

(1) P -> ε
(2) P -> 0
(3) P -> 1
(4) P -> 0P0
(5) P -> 1P1


## Funcionalidades

1. **Generación de Palíndromos:**
   - El usuario puede especificar la longitud del palíndromo o generar uno automáticamente.
   - La longitud máxima del palíndromo es de 100,000 caracteres.

2. **Almacenamiento en Archivo de Texto:**
   - La salida del programa se guarda en un archivo de texto.
   - El archivo especifica qué regla se seleccionó y muestra la cadena resultante hasta llegar a la cadena final.
