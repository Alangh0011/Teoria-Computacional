# Práctica de Teoría Computacional - Programa 2: Protocolo con AFD

## Descripción

Este programa simula el funcionamiento de un protocolo utilizando un Autómata Finito Determinista (AFD). Verifica si el protocolo está encendido o apagado y se ejecuta automáticamente. Genera cadenas binarias aleatorias de longitud 64, se detiene después de cierto criterio y valida cada cadena con el AFD de paridad.

## Funcionalidades

1. **Simulación Automática:**
   - El programa funciona automáticamente.
   - Verifica si el protocolo está encendido o apagado y se ejecuta nuevamente si está encendido.
   - Determina automáticamente cuándo detenerse.

2. **Generación y Validación de Cadenas:**
   - Genera 10^6 cadenas binarias aleatorias de longitud 64.
   - Espera 1 segundo.
   - Valida cada cadena con el AFD de paridad.

3. **Generación de Archivos de Texto:**
   - Tres archivos de texto:
     - Todas las cadenas generadas.
     - Cadenas aceptadas por el AFD.
     - Cadenas rechazadas por el AFD.
   - Si el programa se ejecuta más de una vez, los archivos almacenan los datos de todas las corridas.

4. **Opción de Graficar el AFD Completo:**
   - Opción para graficar el AFD completo, incluyendo el protocolo y la paridad en el mismo grafo.

5. **Iteración del Programa:**
   - El programa verifica si el protocolo está encendido y se ejecuta nuevamente automáticamente.


