'''
    Description: Script en Python que permita lanzar los dados de manera indefinida Y sólo 
    finalizará cuando se genere un PAR de DADOS (1,1 - 2,2 - 3,3 - 4,4 - 5,5 - 6,6)
'''
import os
from random import randint

#Functions
def dices() :
    status = True

    while status :     #while status ==> while status == True
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)

        if dice1 == dice2 :
            status = False
            print("::: Los dados son pares. El lanzamiento ha finalizado :::")
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")    

#Main
dices()