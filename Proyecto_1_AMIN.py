import numpy as np
import time
import sys

Comenzar= time.time()


#Puede o no ocurrir, busca 2 indices al azar y los intercambia
def mutacion(individuo, Prob_mutacion):
    if np.random.rand() < Prob_mutacion:
        n = len(individuo)
        x = np.random.randint(n, size=2)
        individuo[x[0]], individuo[x[1]] = individuo[x[1]], individuo[x[0]]
    return individuo


#repara que no hallan repiticiones, buscando fila a fila un valor unico por posicion
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

#Toma las poblaciones de la ruleta y las cruza desde los indices al azar
def cruza(individuo1, individuo2, Prob_cruza, Prob_mutacion):
    a, b = individuo1.tolist(), individuo2.tolist()
    if random.random() < Prob_cruza:
        n = len(a)
        x = random.randrange(1, n)
        a, b = a[:x] + b[x:], b[:x] + a[x:]
        a, b = reparar_individuo(a), reparar_individuo(b)
        a, b = mutacion(a, Prob_mutacion), mutacion(b, Prob_mutacion)
        print(a,b)

#recorre columnas y revisa choques y sumas cuantos choques hay por tablero
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


#Toma el fitness, y busca mayor fitnes y le da menos proba de aparecer
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

#solicita los datos
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

np.random.seed(semilla)#otorga numeros al azar


#generar poblacion
poblacion= np.zeros([T_poblacion ,T_tablero], dtype=int)  
for i in range(T_poblacion):
    poblacion[i] = np.arange(0,T_tablero)
    np.random.shuffle(poblacion[i])#revuelve los numeros en las posiciones 




print('Ubicacion de las reinas en el tablero')
print(poblacion)

fit=fitness(poblacion)
rul=ruleta(fit)
cruza(poblacion[0], poblacion[1], Prob_cruza, Prob_mutacion)
print('Cantidad de choques por tablero')
print(fit)
print('Porcentajes que da la ruleta por tablero')
print(rul)





    