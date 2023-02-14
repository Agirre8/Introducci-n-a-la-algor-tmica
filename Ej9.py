Algoritmo: Media aritmética

Entrada:
#Los números a promediar son A, B, y C
A, B, C: REAL

Precondición:
A, B, C ≥ 0

Realización:
#Promedio de los números A, B, y C
Resultado <-- (A + B + C) / 3

Poscondición:
Resultado = (A + B + C) / 3

Fin del algoritmo de la media aritmética

Algoritmo: Media aritmética ponderada

Entrada:
#Los números a promediar son A, B, y C
A, B, C: REAL
#Los coeficientes de ponderación son wA, wB, y wC
wA, wB, wC: REAL

Precondición:
A, B, C ≥ 0

0 ≤ wA, wB, wC ≤ 1

Realización:
#Calculamos el promedio ponderado de los números A, B, y C
sumatoria_productos <-- AwA + BwB + C*wC
sumatoria_coeficientes <-- wA + wB + wC
Resultado <-- sumatoria_productos / sumatoria_coeficientes

Poscondición:
Resultado = (AwA + BwB + C*wC) / (wA + wB + wC)

Fin del algoritmo de la media aritmética ponderada