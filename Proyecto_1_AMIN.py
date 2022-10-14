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
    if np.random.rand() < Prob_cruza:
        n = len(a)
        x = np.random.randint(1, n)
        a, b = a[:x] + b[x:], b[:x] + a[x:]
        a, b = reparar_individuo(a), reparar_individuo(b)
        a, b = mutacion(a, Prob_mutacion), mutacion(b, Prob_mutacion)
    return a, b

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
    probabilidad=[]
    for i in fit:
        if i != 0:
            probabilidad.append(1/i)
        else:
            probabilidad.append(0)
    total= sum(probabilidad)
    for i in range(len(probabilidad)):
        probabilidad[i] /= total
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
print("Los valores ingresados son los siguientes:")
print("Semilla:",semilla)
print("Tamaño tablero:",T_tablero)
print("Tamaño poblacion:",T_poblacion)
print("Probabilidad de cruza:",Prob_cruza)
print("Probabilidad de mutacion:",Prob_mutacion)
print("Numero de iteraciones:",N_iteracion)
print("")
print("")
print("Resultados:")

#generar poblacion
poblacion= np.zeros([T_poblacion ,T_tablero], dtype=int)
hijitos = np.zeros([1, T_tablero], dtype=int)
hijitos = np.delete(hijitos, 0, 0)
for i in range(T_poblacion):
    poblacion[i] = np.arange(0,T_tablero)
    np.random.shuffle(poblacion[i]) #revuelve los numeros en las posiciones 
fit=fitness(poblacion)
while 0 not in fit and N_iteracion > 0:
    rul=ruleta(fit)
    while len(hijitos)/T_tablero != len(poblacion):
        while True:
            primerValor, segundoValor = np.random.randint(T_poblacion, size=2)
            if primerValor != segundoValor:
                break
        primero, segundo = cruza(poblacion[primerValor], poblacion[segundoValor], Prob_cruza, Prob_mutacion)
        if len(hijitos)/T_tablero + 2 <= len(poblacion):
            hijitos = np.append(hijitos, primero)
            hijitos = np.append(hijitos, segundo)
        else:
            if np.random.rand() < 0.5:
                hijitos = np.append(hijitos, primero)
            else:
                hijitos = np.append(hijitos, segundo)
    N_iteracion -= 1
    hijitos = np.reshape(hijitos, (T_poblacion, T_tablero))
    poblacion = hijitos
    fit=fitness(poblacion)
    hijitos = np.delete(hijitos, np.arange(len(hijitos)), 0)
if 0 in fit:
    fit = np.array(fit)
    lugar = np.where(fit == 0)
    print("poblacion: ", poblacion[lugar[0][0]])
    print("fitness: ", fit[lugar[0][0]])
else:
    print("No se encontro solucion")






    