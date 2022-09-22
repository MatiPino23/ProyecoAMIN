import numpy as np 
import time
import sys

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
    poblacion[i] = range(0,T_tablero)
    np.random.shuffle(poblacion[i])

print(poblacion)




    