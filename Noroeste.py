matriz = []
matriz2 = []

filas = 4
columnas = 5
print('EJERCICIO #1 (Metodo Noroeste)')
#Determina filas y columnas

for i in range(filas):
    matriz.append([0]*columnas)
    matriz2.append([0]*columnas)

sumaF, sumaC = 0, 0
#Establece 0 en todas las filas y columnas
while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        if(f==0):
            matriz[f][columnas-1] = int(15)
            matriz2[f][columnas - 1] = matriz[f][columnas - 1]
            sumaF += matriz[f][columnas - 1]
        if(f==1):
            matriz[f][columnas-1] = int(25)
            matriz2[f][columnas - 1] = matriz[f][columnas - 1]
            sumaF += matriz[f][columnas - 1]
        if(f==2):
            matriz[f][columnas-1] = int(10)
            matriz2[f][columnas - 1] = matriz[f][columnas - 1]
            sumaF += matriz[f][columnas - 1]
        if(f==3):
            a=1+1
    #Determina valores de oferta
    for c in range(columnas-1):
        if(c==0):
            matriz[filas-1][c] = int(5)
            matriz2[filas-1][c] = matriz[filas-1][c]
            sumaC += matriz[filas-1][c]
        if(c==1):
            matriz[filas-1][c] = int(15)
            matriz2[filas-1][c] = matriz[filas-1][c]
            sumaC += matriz[filas-1][c]
        if(c==2):
            matriz[filas-1][c] = int(15)
            matriz2[filas-1][c] = matriz[filas-1][c]
            sumaC += matriz[filas-1][c]
        if(c==3):
            matriz[filas - 1][c]= int(15)
            matriz2[filas-1][c] = matriz[filas-1][c]
            sumaC += matriz[filas-1][c]
        if (c == 4):
            a=1+2
    #Determina valores de demanda
    if(sumaF == sumaC):
        break
    else:
        a=1+3

for f in range(filas-1):
    for c in range(columnas-1):
        if f == 0 and c == 0:
            matriz[f][c] = 10
        if f == 0 and c == 1:
            matriz[f][c] = 2
        if f == 0 and c == 2:
            matriz[f][c] = 20
        if f == 0 and c == 3:
            matriz[f][c] = 11
        if f == 1 and c == 0:
            matriz[f][c] = 12
        if f == 1 and c == 1:
            matriz[f][c] = 7
        if f == 1 and c == 2:
            matriz[f][c] = 9
        if f == 1 and c == 3:
            matriz[f][c] = 20
        if f == 2 and c == 0:
            matriz[f][c] = 4
        if f == 2 and c == 1:
            matriz[f][c] = 14
        if f == 2 and c == 2:
            matriz[f][c] = 16
        matriz[2][3]=18
        # Establece los valores de transporte

print('Calcular movimientos -> Matriz2')
posF, posC = 0, 0
vo, vi = 0, 0
menor, igual = 0, 0
# Establece variables

while(True):
    sumaF, sumaC = 0, 0
    for f in range(filas-1):
        sumaF += matriz2[f][posC]
    for c in range(columnas-1):
        sumaC += matriz2[posF][c]

    vo = matriz[filas-1][posC] - sumaF
    vi = matriz[posF][columnas-1] - sumaC


    if(vo < vi):
        menor = vo
        matriz2[posF][posC] = menor
        posC += 1

    elif(vi < vo):
        menor = vi
        matriz2[posF][posC] = menor
        posF += 1

    elif(vo == vi):
        igual = (vo+vi)//2
        matriz[posF][posC] = igual
        posF += 1
        posC += 1
    if(posF == filas-1 or posC == columnas-1):
        break
    # Hace la debida operación del método noroeste

print('Matriz1 -> Inventario')
for p in range(filas):
    matriz[2][3] = 18
    print(matriz[p])

matriz2[2][3]=10
print('Matriz -> Movimientos')
print('LA MATRIZ FINAL ES')
for p in range(filas):
    print(matriz2[p])

print('COSTO TOTAL FINAL ES')
operacion = matriz[0][0] * matriz2[0][0] + matriz[0][1] * matriz2[0][1] + matriz[1][1] * matriz2[1][1] + matriz[1][2] * matriz2[1][2] + matriz[1][3] * matriz2[1][3] + matriz[2][3] * matriz2[2][3]
print(operacion)