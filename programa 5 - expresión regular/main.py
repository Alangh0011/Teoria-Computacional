import itertools
from sys import exit
import random

separador = '°'*50
x = []
y = []

while True:
    lista = ["0", "10"]
    listavac = ['e']
    listaux = []
    print('\n\n%sMenu%s' % (separador, separador))
    print("""
        1.- Generar 10 cadenas 
        2.- Salir
    """)
    opc = int(input("Selecciona una opcion valida: "))

    if (opc == 1):
        num = 10
    elif (opc == 2):
        print("""Salimos......
        """)
        exit()
    else:
        print('Opción no válida')
        continue

    for repet in range(num):
        permutations = list(itertools.product(lista, repeat=repet + 1))
        listavac.append(permutations)
    for i in range(num + 1):
        listaux.extend(listavac[i])
    else:
        j = (len(listaux) - 1)
        u = 0
        z = []
        while u <= j:
            z.append(''.join([str(elem) for elem in listaux[u]]))
            u += 1
        x.append(num)
        y.append((num - 1) * pow(2, num) + 1)

    for i in z:
        numUnion = random.choice(range(1,4))
        if(numUnion == 1):
            i = i + '1'
        elif(numUnion == 2):
            i = i + '0'
        else:
            i = i + ' '
    aux = 1
    f = open("Cadenas.txt", "a+")
    f2 = open("Operaciones.txt", "a+")
    while (aux<=10):
        numaux = random.choice(range(len(z)))
        print(z[numaux])
        f.write(f'{z[numaux]} ')
        if(z[numaux][-1] == ' '):
            desc = 'e'
        else:
            desc = z[numaux][-1]
        f2.write(f'(L^{numaux})*({desc})\n')
        aux+=1
    f.close()
    f2.close()
