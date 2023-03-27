def comb(lista):
    n = len(lista)
    grupo_1 = []
    grupo_2 = []
    grupo_3 = []
    all_grupos = []
    for i in range(1,n-1):
        grupo_1 = lista[0:i]
        for j in range(1,n-i):
            grupo_2 = lista[i:i+j]
            grupo_3 = lista[i+j:]
            #print(grupo_1, grupo_2, grupo_3)
            temp = []
            temp.append(grupo_1)
            temp.append(grupo_2)
            temp.append(grupo_3)
            all_grupos.append(temp)

    return all_grupos

def verificando_max(lista, p_max):
    maxx_list = []
    for i in lista:
        maxx_list.append(sorted(i)[3-p_max])
    #print(max_list)
    '''maxii = 0
    for m in maxx_list:
        if m > maxii:
            maxii = m
    '''
    print(maxx_list)
    return maxx_list



def main():
    lista_tensoes = input().split()

    lista_tensoes = list(map(int, lista_tensoes))

    todos_os_gps = comb(lista_tensoes)
    #print(todos_os_gps)


    listaaa = []
    for i in range(len(todos_os_gps)):
        tmpp = []
        for j in range(len(todos_os_gps[i])):
            somaPow=0
            for k in range(len(todos_os_gps[i][j])):
                
                somaPow = somaPow + (todos_os_gps[i][j][k])**2
            thd = ((somaPow**(1/2))/220)*100
                #print(thd)
            thd = (f'{thd:.2f}')
            tmpp.append(thd)
        listaaa.append(tmpp)

    
    for i in range(len(listaaa)):
        for j in range(len(listaaa[i])):
            listaaa[i][j] = float(listaaa[i][j])
    
    max_list = verificando_max(listaaa, 1)

    minimo = 1000000000000000000000
    contador = 0
    for m in max_list:
        if m < minimo:
            minimo = m

    for j in max_list:
        if j == minimo:
            contador+=1
    #print(contador)
    if contador == 2:
        max_list = verificando_max(listaaa, 2)
    #print(max_list)
    minimo = 1000000000000000000000
    for n in max_list:
        if n < minimo:
            minimo = n
    
    for h in max_list:
        if h == minimo:
            contador+=1
    if contador == 3:
        max_list = verificando_max(listaaa, 3)

    #print(max_list)
    #print(contador)
    #print(listaaa.sort())
    #print(max_list)
main()