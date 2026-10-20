import os
import time
import random

cuenta = []
dinero = 10000

ct = random.randint(10000,99999)
cuenta.append(ct)

cajero = True

def menu():
        os.system('cls')
        print("""
==============================
       CAJERO AUTOMÁTICO
==============================
1. Consultar cuenta
2. Consultar saldo
3. Depositar dinero
4. Retirar dinero
5. Salir
==============================
Seleccione una opción:
        """)

def salida():
    os.system('cls')
    print("""
==============================
       CAJERO AUTOMÁTICO
==============================
Gracias por usar nuestro cajero \nVuelva pronto!!
                    """)

def cc():
    os.system('cls')
    print(f"""
==============================
       CAJERO AUTOMÁTICO
==============================
Su numero de cuenta es: {cuenta[0]}
==============================
1. Regresar al menú
2. Salir
        """)

def cs():
     os.system('cls')
     print("""
==============================
       CAJERO AUTOMÁTICO
==============================
Ingrese su numero de cuenta:
1. Volver al menu
            """)
def sd():
    os.system('cls')
    print(f"""
==============================
       CAJERO AUTOMÁTICO
==============================
Su numero de cuenta es: {cuenta[0]}
Su saldo actual es de: ${dinero:,}
==============================
1. Volver al menu
2. Salir
                    """)

def dep(d="depositar"):
    os.system('cls')
    print(f"""
==============================
       CAJERO AUTOMÁTICO
==============================
Ingrese la cantidad que desea {d}:
""")

def sda():
    os.system('cls')
    print("""
==============================
       CAJERO AUTOMÁTICO
==============================
Saldo actualizado correctamente
Presione ENTER para continuar
""")

def fd():
    os.system('cls')
    print("""
==============================
       CAJERO AUTOMÁTICO
==============================
Usted no cuenta con fondos suficientes
==============================
1. Regresar al menú
2. Salir
""")

def dpm(d="depositar"):
    os.system('cls')
    print(f"""
==============================
       CAJERO AUTOMÁTICO
==============================
Introduzca una cantidad valida
Solo se permite {d} desde $5000
Solo se permite {d} maximo $1,000,000
==============================
Ingrese la cantidad que desea {d}:
""")

while cajero:  
    menu() 
    op = int(input())
    while op > 5 or op <=0:
        os.system('cls')        
        menu()
        print("Por favor escoja una opcion valida \n")
        op = int(input())
    if op == 1:
        cc()
        opc = int(input())
        while opc > 2 or opc <=0:
            print("Por favor escoja una opcion valida")
            opc = int(input())
        if opc == 1:
            print("")
        elif opc == 2:
            salida()
            break

    elif op == 2:
        cs()
        nc = int(input())
        if nc == 1:
            print("")
        else:
            while nc != (cuenta[0]):
                cs()
                print("Ingrese un numero de cuenta valido")
                nc = int(input())
                if nc == 1:
                    break
            if nc == 1:
                continue
            sd()
            ops = int(input())
            while ops > 2 or ops <=0:
                print("Por favor escoja una opcion valida")
                ops = int(input())
            if ops == 1:
                print("")
            elif ops == 2:
                salida()
                break

    elif op == 3:
        cs()
        nc = int(input())
        if nc == 1:
            print("")
        else:
            while nc != (cuenta[0]):
                cs()
                print("Ingrese un numero de cuenta valido")
                nc = int(input())
                if nc == 1:
                    break
            if nc == 1:
                continue
            dep()
            dp = int(input())
            while dp < 5000 or dp > 1000000:
                os.system('cls')
                dpm()
                dp = int(input())
            dinero = dinero + dp
            sda()
            ont = input()

    elif op == 4:
        cs()
        nc = int(input())
        if nc == 1:
            print("")
        else:
            while nc != (cuenta[0]):
                cs()
                print("Ingrese un numero de cuenta valido")
                nc = int(input())
                if nc == 1:
                    break
            if nc == 1:
                continue
            if dinero < 5000:
                fd()
                op = int(input())
                while op >2 or op <=0:
                    fd()
                    print("Por favor escoja una opcion valida")
                    op = int(input())
                if op == 1:
                    continue
                elif op == 2:
                    salida()
                    break 
            dep(d="retirar")
            dp = int(input())
            while dp > 1000000 or dp < 5000:
                os.system('cls')
                dpm(d="retirar")
                dp = int(input())  
            if dp > dinero:
                fd()
                op = int(input())
                while op > 2 or op <=0:
                    fd()
                    print("Por favor escoja una opcion valida")
                    op = int(input())
                if op == 1:
                    continue
                elif op == 2:
                    salida()
                    break
            dinero = dinero - dp
            sda()
            ont = input()
    elif op == 5:
        salida()
        break
        
marca = [
    (""" ==============
|    Code by   |
|    JORKENN   |
 ==============
 """,0.02)
]

for letra, tiempo in marca:
    for let in letra:
        print(let, end="", flush=True)
        time.sleep(tiempo)