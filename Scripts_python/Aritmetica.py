'''
    Developer: jayala
    Description: Script que recibe dos números por consola y permite seleccionar de un menú,
    una opción de operación aritmética a realizar con los números ingresados.
    Las operaciones son: Suma, Resta, Multiplicación, División.
'''
import os

#Functions
def menu() :
    print("::: MENU :::")
    print("[1.] Sumar")
    print("[2.] Restar")
    print("[3.] Multiplicar")
    print("[4.] Dividir")
    print("[5.] Cancelar operación")

def calculadora(x, y, z):
    if z == '1' :
        ans = x + y
    elif z == '2' :
        ans = x - y
    elif z == '3' :
        ans = x * y
    elif z == '4' :
        ans = x / y
    elif z == '5' :
        print("La operación ha sido cancelada")
        ans = 0
    else :
        print(".:: OPCIÓN INCORRECTA ::.")
        ans = 0

    #print("El resultado de la operación es: ", ans)                 
    return ans

#Main
os.system("clear")
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
menu()

op = input(".:: Digite una opción: ")
res = calculadora(n1, n2, op)
print("El resultado de la operación es: ", res)