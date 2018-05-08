import matplotlib.pyplot as plt
import numpy as np
from random import shuffle

def sort_doors():
	a=['goat','goat','car']#creo la lista
	shuffle(a)#modifico el arreglo (lo desordeno)
	return a#devuelvo la lista desordenada
def choose_door():
	return np.random.choice(3)#retorna aleatorio entre 0 1 y 2


def reveal_door(lista, choice):
	for i in range(len(lista)):#recorre la lista
		if i!=choice and lista[i]=='goat':#si no esta en choice y es goat
			lista[i]='GOAT_MONTY'#cambia cabra por la revelada
			return lista#retorna antes de seguir el for

def finish_game(lista, choice, change):
	if change:#si se quiere cambiar
		for i in range(len(lista)):
			if i!=choice and lista[i]!='GOAT_MONTY':
				return lista[i]#retorna el que no es chice ni goatmonty
	else:#si no quiere cambiar
		return lista[choice]#retorna en choice

N=10000
cambia=np.zeros(N).astype(str)#array de strings que guarda el resultado si cambia
nocambia=np.zeros(N).astype(str)#arrat de strings que guarda los resultados si no cambia
for i  in range(N):
	lista=sort_doors()#creo la lista
	choice=choose_door()#elijo
	lista=reveal_door(lista,choice)#modifico la lista revelando la puerta con GOAT_MONTY
	cambia[i]=finish_game(lista,choice,True)#si cambia pues le bota el resutado si cambia
	nocambia[i]=finish_game(lista,choice,False)#al reves
print 'Probabilidad de obtener el premio cuando NO hubo cambio de puerta: '+str(1.0*len(nocambia[nocambia=='car'])/(1.0*N))
print 'Probabilidad de obtener el premio cuando SI hubo cambio de puerta: '+str(1.0*len(cambia[cambia=='car'])/(1.0*N))
