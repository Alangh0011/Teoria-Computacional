
# -*- coding: utf-8 -*-
from __future__ import print_function
from Pila import automata
import random

separador = '='*50
def iniciar():
    continuar = True
    while continuar:
        opcion = imprimir_menu()
        if opcion == 1:
            entrada_consola()
        elif opcion == 2:
            ejecutar_random()
        else:
            break # Sal del programa
        print('=' * 100)
        opcion = input("Reintentar [s/n]: ")
        if opcion.lower() != 's':
            continuar = False

    print('Saliendo del programa...')

def imprimir_menu():
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Entrada en consola (Manual)
        2.- Aleatorio (Automatico)
        3.- Salir
    """)
    try:
        opcion = int(input("Selecciona una opcion valida: "))
        return opcion
    except Exception as e:
        print('Error ', e)
        return 0

def entrada_consola():
    texto = input("Escribe el numero binario: ")
    animacion = ver_animacion()
    automata(texto, animacion)

def ver_animacion():
    opcion = input("Ver animacion [s/n]: ")
    if opcion == 's':
        return True
    else:
        return False

def ejecutar_random():
    i = 0
    longitud_random = random.randint(1, 1000)
    numero_binario = ''
    while i < longitud_random:
        numero_binario += random.choice(['0', '1'])
        i += 1

    print("El numero aleatorio es: ", numero_binario)
    animacion = ver_animacion()
    automata(numero_binario, animacion)

iniciar()