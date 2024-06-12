from funciones_test import*
import os
os.system('cls')
trabajadores=[]
while True:
    print("MENU")
    print("1. Registrar trabajador")
    print("2. Lista de todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    opc=int(input("ingrese opcion: "))
    opciones(opc)