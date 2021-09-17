'''
Reto:
Requerimiento del script:
-> Un solo jugador lanza los dados
-> Debe recorrer de cero (0) a cien posiciones (100)
-> El puede terminar cuando:
    - Cuando el jugador obtenga dos partes consecutivas
    - Cuando llegue a la meta (100+) 
'''
import os
from random import randint

#Functions
def dices() :
    status = True

    while status :     
        os.system("clear")
        dice1 = randint(0,100)
        dice2 = randint(0,100)
        result = (dice1+dice2)
        result2 = (result)
        result3 = (dice1+dice2+result)
        print("D1: ", dice1)
        print("D2: ", dice2)


        if dice1 + dice2 >= 100 :
            status = False
            print("->Llego a cien o más de cien. El lanzamiento ha finalizado:", result)
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")
            if result < 100:
                print("-> La suma es:", result2)
            else :
                key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")
                if result3 >= 100:
                    print ("->El lanzamiento ha finalizado:", dice1+dice2+result2)    
            

#Main
dices()