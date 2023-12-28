# Práctica de Teoría Computacional - Programa 3: Tablero de Ajedrez

## Descripción

Este programa permite realizar movimientos ortogonales y diagonales en un tablero de ajedrez de 4x4 con una pieza. Los movimientos y reglas están basados en el curso de Stanford.

## Funcionalidades

1. **Modo Automático y Manual:**
   - El programa puede ejecutarse en modo automático y manual.
   - En el modo manual, el usuario introduce la cadena de movimientos.
   - En el modo automático, el programa genera aleatoriamente la cadena, con un máximo de 100 caracteres o 20 movimientos, según la elección del usuario.

2. **Automata No Determinista (NFA):**
   - Se implementa un NFA para representar el tablero y los movimientos de la pieza.
   - El estado inicial es el estado 1 y el estado final es el estado 16.

3. **Generación de Archivos de Movimientos:**
   - Se generan archivos con todos los movimientos posibles y otro archivo con los movimientos ganadores.

4. **Dibujo del Tablero y Animación:**
   - Se dibuja el tablero y se muestran los movimientos de dos jugadas seleccionadas aleatoriamente de los movimientos ganadores.
   - Para la animación, se sugiere utilizar un bitmap para la pieza o dibujar un círculo dentro del cuadrado y simular el movimiento.

