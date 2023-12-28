# Práctica de Teoría Computacional - Programa 4: Buscador de Palabras

## Descripción

Este programa implementa un autómata finito determinístico (AFD) para reconocer palabras específicas en un texto. Las palabras a reconocer son: web, webpage, website, webmaster, webhome, ebay, coin.

## Funcionalidades

1. **Diseño del NFA y Conversión a DFA:**
   - Se diseña un NFA para reconocer las palabras clave.
   - Se realiza la conversión a un DFA, mostrando todo el proceso a través de las tablas.

2. **Lectura de Archivo o Cadena de Usuario:**
   - El programa lee un archivo de texto como entrada o permite al usuario definir una cadena.

3. **Identificación de Palabras Reservadas:**
   - El AFD identifica cada palabra reservada en el texto.
   - Cuenta las ocurrencias y señala la posición de cada palabra.

4. **Generación de Archivo con Resultados:**
   - Se genera un archivo que enumera, cuenta y anota la posición de las palabras encontradas.

5. **Historia del Proceso del AFD:**
   - Se imprime un archivo que muestra la evaluación del autómata por cada carácter leído, incluyendo cambios de estado.

6. **Visualización del Grafo del Autómata:**
   - El programa proporciona la opción de ver el grafo del autómata utilizado.

