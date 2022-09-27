import numpy as np 
import time
import sys

def fitness(tablero):
    rows, columns= tablero.shape
    count = 0
    list = []
    for tab in tablero:
        for i in range(columns-1):
            for j in range(i+1,columns):
                if abs(tab[i]-tab[j]) == abs(i-j):
                    count += 1
        list.append(count)
        count = 0
    return list

Comenzar= time.time()

if len(sys.argv)==7:
    semilla=int(sys.argv[1])
    T_tablero=int(sys.argv[2])
    T_poblacion=int(sys.argv[3])
    Prob_cruza=float(sys.argv[4])
    Prob_mutacion=float(sys.argv[5])
    N_iteracion=int(sys.argv[6])
else:
    print('Error de parametros ingresados')
    sys.exit(0)

np.random.seed(semilla)

poblacion= np.zeros([T_poblacion ,T_tablero], dtype=int)  
for i in range(T_poblacion):
    poblacion[i] = np.arange(0,T_tablero)
    np.random.shuffle(poblacion[i])

print(poblacion)

fit=fitness(poblacion)

print(fit)



    