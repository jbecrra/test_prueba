import time

def menu():
        print("MENU")
        print("1. Registrar trabajador")
        print("2. Lista de todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del programa")
        
def opc_1(lista_p):
        nombre=input("nombre: ") 
        cargo=input("cargo: ") 
        sueldo=int(input("sueldo bruto: "))
        salud=sueldo//7
        afp=sueldo//12
        trabajador={"nombre":nombre,"cargo":cargo,"sueldo bruto":sueldo,"desc salud":salud,"desc afp":afp, "liquido a pagar":sueldo-salud-afp}
        lista_p.append(trabajador)        
        return lista_p    
def opc_2():
    print




def opciones(opc):
    trabajadores=["nombre"]
    while True:
        try:
            if opc in(1,2,3,4):
                break
            else:
                print("ERROR! debe ingresar una opcion del menú")
        except:
            print("ERROR debe inresar un numero entero")
    if opc==1:
        opc_1(trabajadores)
    elif opc==2:
        print("LISTA DE LOS TRABAJADORES")
        for x in range(len(trabajadores)):
            print(trabajadores[x])
    elif opc==3:
        print("IMPRIMIR PLANILLA DE SUELDOS")
    else:
        print("adios")
    time.sleep(3)
