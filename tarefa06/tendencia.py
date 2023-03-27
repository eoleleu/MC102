def verificar_outliers(desvio_padrao_por_ano, lista_temperatura_ordenada, lista_temperatura_media_por_ano):

    outliers = []
    lista_index = []

    for i in range(0, 168, 12):
        j = i
        while j < (i+12):
            if not (float(lista_temperatura_ordenada[j]) >= lista_temperatura_media_por_ano[i//12] - 1.5*desvio_padrao_por_ano[i//12] 
            and float(lista_temperatura_ordenada[j]) <= lista_temperatura_media_por_ano[i//12] + 1.5*desvio_padrao_por_ano[i//12]):
                outliers.append(lista_temperatura_ordenada[j])

                lista_index.append(j)
            j+=1

    #print(lista_index)

    return lista_index

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
    
    outliers = verificar_outliers(desvio_padrao_por_ano, lista_temperatura_ordenada, lista_temperatura_media_por_ano)
   
    print('Outliers:')
    for i in outliers:
        print(lista_data_ordenada[i])

    print()
    print('Tendência de média anual:')

    lista_tendencia = []
    for i in range(0,168, 12):
        j = i
        soma = 0
        cont = 0
        while j < (i+12):
            if j not in outliers:
                
                soma = soma + float(lista_temperatura_ordenada[j])
                cont += 1

            j+=1
        media = float(soma/cont)
        lista_tendencia.append(media)

    ano = 2000
    for x in lista_tendencia:
        print(f'{ano}'+': '+ f'{ x:.2f}')
        ano+=1
    

    #print(lista_ordenada)
    #print(lista_temperatura_ordenada)
    #print(desvio_padrao_por_ano)
    #print(outliers)
    #print(lista_temperatura_ordenada)
    #print(lista_temperatura_media_por_ano)

main()