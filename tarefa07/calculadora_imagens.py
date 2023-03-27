import copy

def criar_matriz(imagem):
    with open(f"dados/{imagem}") as imagem1: 
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa07/

        texto = imagem1.readline()

        comentario = imagem1.readline()

        dimensoes = imagem1.readline()

        intensidade_do_branco = imagem1.readline()
        
        matriz = []


        for linha in imagem1:
            if linha != '':
                matriz.append([*map(int, linha.strip().split())])
            else:
                break


        
    return matriz

def gravar_arquivo(arq, matriz):
    arquivo = open(f"{arq}", 'w')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa07/
    nome = arq.split('/')[1]
    strr = f'P2\n# testes/{nome}\n{len(matriz[0])} {len(matriz)}\n255\n'

    for i in matriz:
        strr += ' '.join(list(map(str,i))) + '\n'
    arquivo.write(strr)

    arquivo.close()

    return arquivo

def filtro_laplaciano(a, id):
    filtro_laplace = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    
    #print(a[0])


    matriz_novaa = copy.deepcopy(a)

    for i in range(len(matriz_novaa)):
        for j in range(len(matriz_novaa[0])):
            if((i == 0 or j == 0 or i == len(matriz_novaa) -1 or j == len(matriz_novaa[0]) -1)):
                matriz_novaa[i][j] = 0
            else:
                tmp = 0
                for l in range(-1,2):
                    for c in range(-1,2):
                        #print(l,c,i,j,len(a),len(a[0]))
                        tmp +=  filtro_laplace[l + 1][c + 1] * a[i + l][j + c]
                matriz_novaa[i][j] = tmp

    #print(a[0])
    print(contPixelsMaiorZero(matriz_novaa, id))

    return matriz_novaa

def filtro_gaussiano(w, id):
    filtro_gauss = [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]]

    matriz_novaaa = copy.deepcopy(w)

    for i in range(len(matriz_novaaa)):
        for j in range(len(matriz_novaaa[0])):
            if (i == 0 or j == 0 or i == len(matriz_novaaa) -1 or j == len(matriz_novaaa) -1):
                matriz_novaaa[i][j] = 0
            else:
                tmp1 = 0
                for l in range(-2, 3):
                    for c in range(-2, 3):
                        tmp1 +=  filtro_gauss[l+2][c+2] * w[i + l][j + c]
                matriz_novaaa[i][j] = tmp1

    print(contPixelsMaiorZero(matriz_novaaa, id))

    return matriz_novaaa

def normalizar(matriz_imagemN, id):

    maximo = 0
    minimo = 255



    
    for i in range(len(matriz_imagemN)):
        for j in matriz_imagemN[i]:
            j = int(j)
            if j > maximo:
                maximo = j 
            
            if j < minimo:
                minimo = j
    
    for i in range(len(matriz_imagemN)):
        for j in range(len(matriz_imagemN[i])):
            matriz_imagemN[i][j] = (255*(matriz_imagemN[i][j] - minimo))/(maximo - minimo)
            matriz_imagemN[i][j] = int(matriz_imagemN[i][j] // 1) 
            

    print(contPixelsMaiorZero(matriz_imagemN, id))

    return matriz_imagemN

def somar(mat1, mat2, id):

    l = len(mat1)
    c = len(mat1[0])

    mat3_S = [[0 for j in range(c) ] for i in range(l)]

    for i in range(l):
      for j in range(c):
          mat3_S[i][j] = (int(mat1[i][j]) + int(mat2[i][j]))//2

    print(contPixelsMaiorZero(mat3_S, id))
    return mat3_S

def binarizar_matriz(matriz_imagemB, limiar, id):

    limiar = int(limiar)

    for i in range(len(matriz_imagemB)):
        for j in range(len(matriz_imagemB[i])):
            if int(matriz_imagemB[i][j]) <= limiar:
                matriz_imagemB[i][j] = 0
            
            if int(matriz_imagemB[i][j]) > limiar:
                matriz_imagemB[i][j] = 255

    print(contPixelsMaiorZero(matriz_imagemB, id))

    return matriz_imagemB

def multiplicar_matriz(mat1, mat2, id):
    l = len(mat1)
    c = len(mat1[0])

    mat3 = [[0 for j in range(c) ] for i in range(l)]

    for i in range(l):
      for j in range(c):
          mat3[i][j] = int(mat1[i][j]) * int(mat2[i][j])

    print(contPixelsMaiorZero(mat3, id))
    return mat3

def contPixelsMaiorZero(matriz, id):
    n = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if int(matriz[i][j]) > 0:
                n += 1

    return f'Imagem {id} modificada: {n} pixels maiores que zero.'

def main():

    entradas = []
    lista_matriz_imagens = []
    lista_binarizar = []

    lista_carregar = []


    lista_multiplicar = []
    lista_normalizar = []

    lista_gravar = []

    while True:
        
        aux = []
        try: 
            line = input()
        except: 
            break
        aux.append(line)
        entradas.append(aux)
        '''
        aux = []
        line = input()
        if line == '': 
            break
        aux.append(line)
        entradas.append(aux)
        '''

    for k in range(len(entradas)):
        
        if entradas[k][0][0:8] == 'carregar':
            a = (entradas[k][0])
            #lista_carregar.append(a)
            nome = a.split('/')[1]
            id = len(lista_matriz_imagens)
            print(f'Carregado arquivo dados/{nome} em imagem {id}.')
            lista_matriz_imagens.append(criar_matriz(nome))

        if entradas[k][0][0:9] == 'binarizar':
            b = (entradas[k][0])
            id = int(b.split(' ')[1])
            limiar = b.split(' ')[2]
            matriz_imagemA = copy.deepcopy(lista_matriz_imagens[id])
            lista_matriz_imagens[id] = binarizar_matriz(matriz_imagemA, limiar, id)
            #lista_carregar.append(b)

        if entradas[k][0][0:11] == 'multiplicar':
            c = (entradas[k][0])
            id1 = int(c.split(' ')[1])
            id2 = int(c.split(' ')[2])
            matriz_imagemA = copy.deepcopy(lista_matriz_imagens[id1])
            matriz_imagemB = copy.deepcopy(lista_matriz_imagens[id2])
            lista_matriz_imagens[id1] = multiplicar_matriz(matriz_imagemA, matriz_imagemB, id1)
            #lista_multiplicar.extend(c)

        if entradas[k][0][0:5] == 'somar':
            f = (entradas[k][0])
            id1 = int(f.split(' ')[1])
            id2 = int(f.split(' ')[2])
            matriz_imagemA = copy.deepcopy(lista_matriz_imagens[id1])
            matriz_imagemB = copy.deepcopy(lista_matriz_imagens[id2])
            lista_matriz_imagens[id1] = somar(matriz_imagemA, matriz_imagemB, id1)

        if entradas[k][0][0:10] == 'normalizar':
            d = (entradas[k][0])
            id = int(d.split(' ')[1])
            matriz_imagemA = copy.deepcopy(lista_matriz_imagens[id])
            lista_matriz_imagens[id] = normalizar(matriz_imagemA, id)
            #lista_normalizar.extend(d)

        if entradas[k][0][0:7] == 'filtrar':
            e = (entradas[k][0])
            id = int(e.split(' ')[1])
            filtro = e.split(' ')[2]
            matriz_imagemA = copy.deepcopy(lista_matriz_imagens[id])
            if filtro == 'Gaussiano':
                lista_matriz_imagens[id] = filtro_gaussiano(matriz_imagemA, id)
            else:
                lista_matriz_imagens[id] = filtro_laplaciano(matriz_imagemA, id)

            #lista_normalizar.extend(d)

        if entradas[k][0][0:6] == 'gravar':
            q = (entradas[k][0])
            id = int(q.split(' ')[2])
            local = q.split(' ')[1]
            matriz = copy.deepcopy(lista_matriz_imagens[id])
            gravar_arquivo(local, matriz)
            print(f'Gravado arquivo {local} com imagem {id}.')
    
main()