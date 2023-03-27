def calcular_discrepancia(desvio_padrao_por_mes, lista_temperatura_ordenada, lista_temperatura_media_por_mes):

    lista_discrepancia = [0,0,0,0,0,0,0,0,0,0]
    lista_index = [0,0,0,0,0,0,0,0,0,0]
    indice_minimo = 0

    for j in range(0, 12):
        for i in range(0, 14):
                discrepancia = (abs(float(lista_temperatura_ordenada[i*12+j]) - float(lista_temperatura_media_por_mes[j]))/float(desvio_padrao_por_mes[j]))
                
                for elemento in lista_discrepancia:
                    if elemento < discrepancia:
                        lista_discrepancia[indice_minimo] = discrepancia
                        lista_index[indice_minimo] = i*12+j
                        for i in range(len(lista_discrepancia)):
                            if lista_discrepancia[i] < lista_discrepancia[indice_minimo]:
                                indice_minimo = i
                                
                        break
            
    '''
    lista_discrepancia = []

    for j in range(0, 12):
        for i in range(0, 14):
                discrepancia = (abs(float(lista_temperatura_ordenada[i*12+j]) - float(lista_temperatura_media_por_mes[j]))/float(desvio_padrao_por_mes[j]))
                
                lista_discrepancia.append(discrepancia)
    '''

    return lista_discrepancia, lista_index

def calcular_desvio_padrao_por_mes( lista_temperatura_ordenada, lista_temperatura_media_por_mes):

    desvio_padrao_por_mes = []
        
    for j in range(0, 12):
        soma = 0
        for i in range(0, 14):
            soma += (float(lista_temperatura_ordenada[i*12+j]) - float(lista_temperatura_media_por_mes[j]))**2
 
        soma = soma/14

        desvio_padrao = raiz_quadrada(soma)

        desvio_padrao_por_mes.append(desvio_padrao)   
    return desvio_padrao_por_mes

def calcular_temperatura_media_por_mes(lista_temperatura_ordenada):
    lista_temperatura_media_por_mes_aux = []
    for j in range(0,12):
        soma = 0

        for i in range(0, 14):
            soma = soma + float(lista_temperatura_ordenada[i*12+j])

        lista_temperatura_media_por_mes_aux.append(soma)
    
    lista_temperatura_media_por_mes = []

    for y in lista_temperatura_media_por_mes_aux:
        media = y/14
        lista_temperatura_media_por_mes.append(media)

    return lista_temperatura_media_por_mes

def verificar_discrepancia(desvio_padrao_por_ano, lista_temperatura_ordenada, lista_temperatura_media_por_ano):

    lista_discrepancia = []

    for i in range(0, 168, 12):
        j = i
        while j < (i+12):
            discrepancia = (abs(float(lista_temperatura_ordenada[j]) - float(lista_temperatura_media_por_ano[i//12]))) / (desvio_padrao_por_ano[i//12])
            lista_discrepancia.append(discrepancia)
            j+=1

    return lista_discrepancia

def raiz_quadrada(n):
    raiz = n/2    
    for _ in range(20):
        raiz = (1/2)*(raiz + (n / raiz))

    return raiz

def calcular_desvio_padrao(lista_temperatura_ordenada, lista_temperatura_media_por_ano):

    lista_desvio_padrao = []


    for i in range(0, 168, 12):
        soma = 0
        for temperatura in lista_temperatura_ordenada[i:i+12]:
            temperatura = float(temperatura)
            soma += (temperatura - lista_temperatura_media_por_ano[i//12])**2
            
        soma = soma/12

        desvio_padrao = raiz_quadrada(soma)
        lista_desvio_padrao.append(desvio_padrao)
    
    return lista_desvio_padrao

def calcular_media_por_ano(lista_temperatura_ordenada):

    lista_temperatura_total_por_ano = []

    for i in range(0,168, 12):
        soma = 0.0
        for j in lista_temperatura_ordenada[i:i+12]:
            j = float(j)
            soma = soma + j
        lista_temperatura_total_por_ano.append(soma)

    lista_temperatura_media_por_ano = []

    #print(lista_temperatura_total_por_ano)

    for total in lista_temperatura_total_por_ano:
        media = total/12
        lista_temperatura_media_por_ano.append(media)

    #print(lista_temperatura_media_por_ano)

    return lista_temperatura_media_por_ano

def ordenar_lista(lista_data, lista_temperatura):
    n = len(lista_data)
    for _ in range(n-1):
            for i in range(n-1):
                if lista_data[i][0:2] > lista_data[i+1][0:2]:
                    aux = lista_data[i]
                    lista_data[i] = lista_data[i+1]
                    lista_data[i+1] = aux

                    aux2 = lista_temperatura[i]
                    lista_temperatura[i] = lista_temperatura[i+1]
                    lista_temperatura[i+1] = aux2
    
    for _ in range(n-1):
            for i in range(n-1):
                if lista_data[i][3:7] > lista_data[i+1][3:7]:
                    aux = lista_data[i]
                    lista_data[i] = lista_data[i+1]
                    lista_data[i+1] = aux

                    aux2 = lista_temperatura[i]
                    lista_temperatura[i] = lista_temperatura[i+1]
                    lista_temperatura[i+1] = aux2

    return lista_data, lista_temperatura

def main():
    lista_data = []

    lista_temperatura = []

    pais = input()

    with open(f"{pais}") as arquivo:
        for linha in arquivo:
            data, temperatura = linha.replace('\n','').split(',')
            lista_data.append(data)
            lista_temperatura.append(temperatura)

    lista_data_ordenada, lista_temperatura_ordenada = ordenar_lista(lista_data, lista_temperatura)

    lista_temperatura_media_por_ano = calcular_media_por_ano(lista_temperatura_ordenada)

    desvio_padrao_por_ano = calcular_desvio_padrao(lista_temperatura_ordenada, lista_temperatura_media_por_ano)

    lista_discrepancia = verificar_discrepancia(desvio_padrao_por_ano, lista_temperatura_ordenada, lista_temperatura_media_por_ano)

    lista_temperatura_media_por_mes = calcular_temperatura_media_por_mes(lista_temperatura_ordenada)

    desvio_padrao_por_mes = calcular_desvio_padrao_por_mes(lista_temperatura_ordenada, lista_temperatura_media_por_mes)

    discrepancia, lista_index = calcular_discrepancia(desvio_padrao_por_mes, lista_temperatura_ordenada, lista_temperatura_media_por_mes)
    
    #print(lista_temperatura_ordenada)
    #print(lista_temperatura_media_por_ano)
    #print(desvio_padrao_por_ano)
    #print(lista_discrepancia)
    #print(lista_temperatura_media_por_mes)
    #print(desvio_padrao_por_mes)
    
    #print(lista_index)

    lista_saida_discrepancia = []

    for i in lista_index:
        lista_saida_discrepancia.append(lista_data_ordenada[i])
    
    n = len(lista_saida_discrepancia)
    for _ in range(n-1):
            for i in range(n-1):
                if lista_saida_discrepancia[i][0:2] > lista_saida_discrepancia[i+1][0:2]:
                    aux = lista_saida_discrepancia[i]
                    lista_saida_discrepancia[i] = lista_saida_discrepancia[i+1]
                    lista_saida_discrepancia[i+1] = aux

                    aux2 = discrepancia[i]
                    discrepancia[i] = discrepancia[i+1]
                    discrepancia[i+1] = aux2

    for _ in range(n-1):
            for i in range(n-1):
                if lista_saida_discrepancia[i][3:7] > lista_saida_discrepancia[i+1][3:7]:
                    aux = lista_saida_discrepancia[i]
                    lista_saida_discrepancia[i] = lista_saida_discrepancia[i+1]
                    lista_saida_discrepancia[i+1] = aux

                    aux2 = discrepancia[i]
                    discrepancia[i] = discrepancia[i+1]
                    discrepancia[i+1] = aux2

    #print(discrepancia)
    #print(lista_saida_discrepancia)

    i = 0
    while i < len(lista_saida_discrepancia):
     
        print(f'{lista_saida_discrepancia[i]}'+': '+ f'{discrepancia[i]:.2f}')
        i+=1
main()