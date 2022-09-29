import numpy as np 
import random
import time
import sys

Comenzar= time.time()

def mutacion(individuo, Prob_mutacion):
    if random.random() < Prob_mutacion:
        n = len(individuo)
        x = random.choices(range(n), k=2)
        individuo[x[0]], individuo[x[1]] = individuo[x[1]], individuo[x[0]]
    return individuo

def reparar_individuo(individuo):
    n = len(individuo)
    corrector = [0] * n
    for i in range(n):
        corrector[individuo[i]] += 1
    for i in range(n):
        if corrector[i] == 2:
            for j in range(n):
                if corrector[j] == 0:
                    for k in range(n):
                        if individuo[k] == i:
                            individuo[k] = j
                            corrector[j] += 1
                            corrector[i] -= 1
                            break
                    break
    return individuo

def cruza(individuo1, individuo2, Prob_cruza, Prob_mutacion):
    a, b = individuo1.tolist(), individuo2.tolist()
    if random.random() < Prob_cruza:
        n = len(a)
        x = random.randrange(1, n)
        a, b = a[:x] + b[x:], b[:x] + a[x:]
        a, b = reparar_individuo(a), reparar_individuo(b)
        a, b = mutacion(a, Prob_mutacion), mutacion(b, Prob_mutacion)
        print(a,b)

def fitness(tablero):
    rows, columns= tablero.shape
    count = 0
    lista = []
    for tab in tablero:
        for i in range(columns-1):
            for j in range(i+1,columns):
                if abs(tab[i]-tab[j]) == abs(i-j):
                    count += 1
        lista.append(count)
        count = 0
    return lista

def ruleta (fit):
    total= sum(fit)
    probabilidad=[]
    for i in fit:
        probabilidad.append(i/total)
    ruleta=[]
    ruleta.append(probabilidad[0])
    for j in range(1, len(probabilidad)):
        ruleta.append(ruleta[j-1]+probabilidad[j])
    return ruleta


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





#print(poblacion)

fit=fitness(poblacion)
rul=ruleta(fit)
cruza(poblacion[0], poblacion[1], Prob_cruza, Prob_mutacion)

#print(fit)
#print(rul)





    