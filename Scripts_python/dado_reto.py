'''
Reto: EVELIN VALERIA PADILLA JURADO
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
        newdice1 = randint(0,100)
        newdice2 = randint(0,100)
        result = (dice1+dice2)
        
        print("D1: ", dice1)
        print("D2: ", dice2)
        


        if dice1 + dice2 >= 100 :
            status = False
            print("->Llego a cien o más de cien. El lanzamiento ha finalizado:", result)
        else :
            print("->La sumas es:", result)
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")

            print("D1: ", newdice1)
            print("D2: ", newdice2)

            while result < 100:
                result2 = result + newdice1+newdice2
                print("->La sumas es:", newdice1+newdice2)
                print("Ya llego a la META", result2)
                key = input(".:: finalizado ...") 

#Main
dices()
