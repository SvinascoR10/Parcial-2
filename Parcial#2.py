import random
import numpy as np
from math import pow

def vector1():
    vector1 = []
    for i in range(50):
        vector1.append(random.randint(1,20))
    return vector1

def vector2(vector1):
    vector2 = []
    for i in range(len(vector1)):
        if vector1[i] not in vector2:
            vector2.append(vector1[i])
    return vector2

def vector3(vector1,vector2):
    vector3 = []
    for i in range(len(vector2)):
        vector3.append(vector1.count(vector2[i]))
    return vector3

def porteclado(vector1,dato):
    contador = 0
    for i in range(len(vector1)):
        if vector1[i] == dato:
            contador += 1
    return contador

#Función que hace una matriz de 5x5 con valores aleotorios entre 100 y 200 con numpy
def matriz():
    matriz = np.random.randint(1,5,(5,5))
    return matriz

#Función que hace que la matriz anterior devuelva otra matriz pero con los
#elementos de la columna 1 pero elevados al cuadrado seran la fila 1 de la nueva matriz
#y los elementos de la fila 1 pero elevados a la cuarta serna las columnas de la nueva matriz
#y asi sucesivamente hasta llenar la matriz 5x5
def matriz2(matriz):
    matriz2 = np.zeros((5,5))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][0]
            
    return matriz2
def matriz2(matriz):
    matriz2 = np.zeros((5,5))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == 0 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4):
                matriz2[i][j] = pow(matriz[j][i],2)
            elif i ==1 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4):
                matriz2[i][j] = pow(matriz[j][i],4)
            elif i ==2 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4):
                matriz2[i][j] = pow(matriz[j][i],6)
            elif i ==3 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4):
                matriz2[i][j] = pow(matriz[j][i],8)
            elif i ==4 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4):
                matriz2[i][j] = pow(matriz[j][i],10)
    matriz2 = matriz2.astype(int)
    return matriz2

#Función que suma las filas de la matriz 1
def sumar_fila_matriz1(matriz1):
    suma = 0
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            suma += matriz1[i][j]
    return suma

#Función que suma las columnas de la matriz 2
def sumar_columnas_matriz2(matriz2):
    suma = 0
    for j in range(len(matriz2)):
        for i in range(len(matriz2)):
            suma += matriz2[j][i]
    return suma

#Función que multiplica una matriz por un escalar
def matrizxescalar(matrizaleatoria):
    dato = int(input('Ingrese un número entero: '))
    matrizxescalar = np.zeros((5,5))
    for i in range(len(matrizaleatoria)):
        for j in range(len(matrizaleatoria)):
            matrizxescalar[i][j] = matrizaleatoria[i][j] * dato
    return matrizxescalar 

#Función que hace el producto de dos matrices
def producto_dos_matrices(mat1,mat2):
    mat3 = np.zeros((5,5))
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            mat3[i][j] = mat1[i][j] * mat2[i][j]
    return mat3

#Función que calcula la diagonal principal de la matriz 1
def diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                suma += matriz[i][j]
    return suma

#Función que calcula la diagonal inversa de la matriz 2
def diagonal_inversa(matriz2):
    suma = 0
    for i in range(len(matriz2)):
        for j in range(len(matriz2)):
            if i + j == len(matriz2) - 1:
                suma += matriz2[i][j]
    return suma 

#Función que calcula la media de todos los elementos de la matriz multiplicación
def media_matriz_multiplicacion(mat3):
    suma = 0
    for i in range(len(mat3)):
        for j in range(len(mat3)):
            suma += mat3[i][j]
    media = suma / (len(mat3) * len(mat3))
    return media


band = True
entrada_en_1 = True
entrada_en_2 = True 
entrada_en_3 = True
entrada_en_4 = True
entrada_en_6 = True 
entrada_en_7 = True
entrada_en_11 = True
while band == True:
    print('1.Almacenar en un vector 50 números entre 1 y 20.')
    print('2.En un segundo vector, adicionar los números del primero sin repetir.')
    print('3.En un tercer vector imprimir la cantidad de veces que se repite en el primer vector.')
    print('4.Número por teclado e informar cuantas veces se repite en el primer vector.')
    print('5.Contar cuantos elementos tiene cada vector.')
    print('6.Matriz Aleatoria1.')
    print('7.Matriz con los elementos de la primera columna de la matriz aleatoria.')
    print('8.Sumar filas de la matriz 1.')
    print('9.Sumar columnas de la matriz 2.')
    print('10.Calcular el producto de una matriz por un número entero.')
    print('11.Calcular el producto de dos matrices.')
    print('12.Calcualr la diagonal principal de la matriz 1.')
    print('13.Calcular la diagonal inversa de la matriz 2.')
    print('14.Calcular la media de todos los elementos de la matriz multiplicación.')
    print('15.Salir.')
    opcion = int(input('Presione una de las opciones (1,2,3...) para continuar.'))
    print('\n\n')
    if opcion == 1:
        print('Usted ha ingresado a la opción 1.')
        vector1 = vector1()
        print('El vector de números aleatorios es: ',vector1,'\n')
        entrada_en_1 = False
    elif opcion == 2:
        if entrada_en_1 == False:
            print('Usted ha ingresado a la opción 2.')
            vector2 = vector2(vector1)
            print('El vector de números sin repetir es: ',vector2,'\n')
        else:
            print('Usted ha ingresado a la opción 2.\n')
            print('Debe ingresar a la opción 1 primero.\n')
        entrada_en_2 = False
    elif opcion == 3:
        if entrada_en_1 == False and entrada_en_2 == False:
            print('Usted ha ingresado a la opción 3.')
            vector3 = vector3(vector1,vector2)
            print('El vector es: ',vector2,'\n')
            print('El vector de números repetidos es: ',vector3,'\n')
            entrada_en_3 = False
        else:
            print('Usted ha ingresado a la opción 3.\n')
            print('Debe ingresar a la opción 1 y 2 primero.\n') 
    elif opcion == 4:
        if entrada_en_1 == False:
            print('Usted ha ingresado a la opción 4.')
            dato = int(input('Ingrese un número para saber cuantas veces se repite en el primer vector: '))
            contador = porteclado(vector1,dato)
            print('El número',dato,'se repite',contador,'veces en el primer vector.\n')
            entrada_en_4 = False
        else:
            print('Usted ha ingresado a la opción 4.\n')
            print('Debe ingresar a la opción 1 primero.\n')
    elif opcion == 5:
        if entrada_en_1 == False and entrada_en_2 == False and entrada_en_3 == False and entrada_en_4 == False:
            print('Usted ha ingresado a la opción 5.')
            print('El vector de números aleatorios tiene',len(vector1),'elementos.')
            print('El vector de números sin repetir tiene',len(vector2),'elementos.')
            print('El vector de números repetidos tiene',len(vector3),'elementos.\n')
    elif opcion == 6:
        print('Usted ha ingresado a la opción 6.')
        matriz = matriz()
        print('La matriz aleatoria es:\n',matriz,'\n')
        entrada_en_6 = False
    elif opcion == 7:
        if entrada_en_6 == False:
            print('Usted ha ingresado a la opción 7.')
            matriz2 = matriz2(matriz)
            print('La matriz es:\n' ,matriz2,'\n')
        else:
            print('Usted ha ingresado a la opción 7.\n')
            print('Debe ingresar a la opción 6 primero.\n')
        entrada_en_7 = False
    elif opcion == 8:
        if entrada_en_6 == False:
            print('Usted ha ingresado a la opción 8.')
            suma = sumar_fila_matriz1(matriz)
            print('La suma de los elementos de la matriz es: ',suma,'\n')
        else:
            print('Usted ha ingresado a la opción 8.\n')
            print('Debe ingresar a la opción 6 primero.\n')
    elif opcion == 9:
        if entrada_en_7 == False:
            print('Usted ha ingresado a la opción 9.')
            suma1 = sumar_columnas_matriz2(matriz2)
            print('La suma de los elementos de la matriz es: ',suma1,'\n')
        else:
            print('Usted ha ingresado a la opción 9.\n')
            print('Debe ingresar a la opción 7 primero.\n')
    elif opcion == 10:
        matrizaleatoria = np.random.randint(1,5,(5,5))
        print('Usted ha ingresado a la opción 10.\n')
        print('La matriz aleatoria es:\n',matrizaleatoria,'\n')
        mat = matrizxescalar(matrizaleatoria)
        print('La matriz multiplicada por número es:\n',mat,'\n')
    elif opcion == 11:
        mat1 = np.random.randint(1,5,(5,5))
        mat2 = np.random.randint(1,5,(5,5))
        print('Usted ha ingresado a la opción 11.\n')
        print('La matriz 1 es:\n',mat1,'\n')
        print('La matriz 2 es:\n',mat2,'\n')
        mat3 = producto_dos_matrices(mat1,mat2)
        print('La matriz producto de las dos matrices es:\n',mat3,'\n')
        entrada_en_11 = False
    elif opcion == 12:
        if entrada_en_6 == False:
            print('Usted ha ingresado a la opción 12.\n')
            print('La matriz es:\n',matriz,'\n')
            diagonal = diagonal_principal(matriz)
            print('La diagonal principal es:\n',diagonal,'\n')
        else:
            print('Usted ha ingresado a la opción 12.\n')
            print('Debe ingresar a la opción 6 primero.\n')
    elif opcion == 13:
        if entrada_en_7 == False:
            print('Usted ha ingresado a la opción 13.\n')
            print('La matriz es:\n',matriz2,'\n')
            diagonal = diagonal_inversa(matriz2)
            print('La suma de la diagonal inversa es:',diagonal,'\n')
        else:
             print('Usted ha ingresado a la opción 13.\n')
             print('Debe ingresar a la opción 7 primero.\n')

    elif opcion == 14:
        if entrada_en_11 == False:
            print('Usted ha ingresado a la opción 14.\n')
            print('La matriz es:\n',mat3,'\n')
            media = media_matriz_multiplicacion(mat3)
            print('La media de la matriz multiplicación es:',media,'\n')
        else:
            print('Usted ha ingresado a la opción 14.\n')
            print('Debe ingresar a la opción 11 primero.\n')
    elif opcion == 15:
        print('Gracias por estar aqui, te quiero mucho profesor.\n')
        band = False
    else:
        print('Opción incorrecta, vuelva a ingresar otro número.\n')
