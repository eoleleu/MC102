from difflib import Differ

def comparar(arq1, arq2):
    

    diferencass = []

    with open(f'{arq1}') as file_1, open(f"{arq2}") as file_2:
        #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/
        differ = Differ()
  
        for line in differ.compare(file_1.readlines(), file_2.readlines()):
            #print(line)
            diferencass.append(line)
    #print(diferencass)
    

    lista_cima = []
    lista_baixo = []
    for g in range(len(diferencass)):
        if diferencass[g][0] == '-':
            diferencass[g] = diferencass[g].replace('-', '<')
            diferencass[g] = diferencass[g].replace('\n', '')
            lista_cima.append(diferencass[g])
        if diferencass[g][0] == '+':
            diferencass[g] = diferencass[g].replace('+', '>')
            diferencass[g] = diferencass[g].replace('\n', '')
            lista_baixo.append(diferencass[g])
    
    return lista_cima, lista_baixo

def carregar(arquivo_antigo, arquivo_novo):
    '''if arquivo_antigo[len(arquivo_antigo)-3:len(arquivo_antigo)] != 'txt':
            arquivo_antigo = arquivo_antigo + '.txt' '''
    '''if arquivo_novo[len(arquivo_novo)-3:len(arquivo_novo)] != 'txt':
            arquivo_novo = arquivo_novo + '.txt' '''
    #print('-----------')
    #print(arquivo_antigo)
    #print(arquivo_novo)
    file1 = open(f"{arquivo_antigo}", 'r')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/
    conteud = file1.read()
    palavrass = conteud.split('\n')
    #print(palavrass)
    file1.close()

    file2 = open(f"{arquivo_novo}", 'a')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/
    for i in palavrass:
        file2.write(f'{i}'+' \n')
    
    return arquivo_antigo, arquivo_novo

def mostrar(arq):
    arquivo = open(f"{arq}", 'r')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
    conteudoo = arquivo.read()
    word_in_content = conteudoo.split('\n')
    word_in_content.pop(-1)
    for i in range(len(word_in_content)):
        if word_in_content[-1] == '':
            word_in_content.pop(-1)
    print(f'--- início de {arq} ---')
    for i in range(len(word_in_content)):
        word_in_content[i] = word_in_content[i].replace('\n', '')
        print(word_in_content[i])
    print(f'--- final de {arq} ---')

    return arq

def buscar(word, lista):
    contem_or_nao = []
    lista2 = []
    qtdd = 0
    for nome_arquivo in lista:
        arquivo = open(f"{nome_arquivo}", 'r')
        #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
        
        conteudo = arquivo.read()
        palavras_arquivo = conteudo.split(' ')
        for q in range(len(palavras_arquivo)):
            palavras_arquivo[q] = palavras_arquivo[q].replace('\n', '')
        
        #print(palavras_arquivo)
        #print(palavras_arquivo)
        
        if word in palavras_arquivo:
            resultado = True
            lista2.append(nome_arquivo)
            contem_or_nao.append(f' contém')
            qtdd += 1
            
        else:
            resultado = False
            #contem_or_nao.append(f' não contém')
        
        
    #print(contem_or_nao)
    return lista2, contem_or_nao, qtdd

def substituir(entrada):
    old_end = entrada[1]
    '''if entrada[1][len(entrada[1])-3:len(entrada[1])] != 'txt':
            entrada[1] = entrada[1] + '.txt' '''
            #print(entrada)
    #print(entrada)
    arquivo = open(f"{entrada[1]}", 'r+')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
    entrada[2] = str(entrada[2])
    

    old = ''
    for linha in arquivo:
        old += linha.replace(entrada[2],entrada[3])
        

    #print(old)

    arquivo.close()
    entrada.pop(-1)
    entrada.pop(-1)
    entrada.append(old)
    #print(entrada)
    criar_arquivo(entrada[1])
    digitar(entrada)

    arquivo = open(f"{entrada[1]}", 'r+')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
    file = open(f'{entrada[1]}', 'r')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
    counter = 0
    content = file.read()
    Colist = content.split('\n')
    #print(Colist)
    for i in Colist:
        if i:
            counter += 1
    
    #print(Colist)
    
    
    return old_end, counter

def digitar(entrada):
    
    arquivo = open(f"{entrada[1]}", 'a')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/
    string = ''
    for i in entrada[2:]:
        #print(i)
        string = string + ' ' + i
    #print(str)
    arquivo.write(f'{string.strip()}'+' \n')
    

    arquivo.close()

    file = open(f'{entrada[1]}', 'r')
    counter1 = 0
    content = file.read()
    Colist = content.split('\n')
    #print(Colist)
    for i in Colist:
        if i:
            counter1 += 1
    
    return entrada[1], counter1

def criar_arquivo(nome):
    arquivo = open(f"{nome}", 'w')
    #C:/Users/leleu/OneDrive/Documentos/tarefa/ra213437/tarefa08/dados/

    arquivo.close()

    return nome


def main():


    entradas = []
    while True:

        aux = []
        try: 
            line = input().split()
        except: 
            break
        aux.extend(line)
        entradas.append(aux)

        '''aux = []
        line = input().split( )
        if line == []: 
            break
        aux.extend(line)
        entradas.append(aux)'''
        
    lista_arq_criados = []
    lista_arq_criados2 = []
    admin = [0]
    arq_criados = 0
    for k in range(len(entradas)):

        if entradas[k][0] == 'entrar':
            admin[0] = entradas[k][1]
            print(f'{entradas[k][1]} entrou!')

        if entradas[k][0] == 'criar':
            lista_arq_criados.append(f'{entradas[k][1]}'+ f' {admin[0]}')
            lista_arq_criados2.append(f'{entradas[k][1]}')
            arq_criados += 1
            nome_arquivo = criar_arquivo(entradas[k][1])
            print(f'{nome_arquivo} criado')
        

        if entradas[k][0] == 'digitar':

            modificado, contador1 = digitar(entradas[k])

            print(f'{modificado} modificado: {contador1} linhas')

        if entradas[k][0] == 'substituir':
            
            modificado1, contador2 = substituir(entradas[k])
            print(f'{modificado1} modificado: {contador2} linhas')

        if entradas[k][0] == 'buscar':
            #print(entradas[k][0])
            #buscado, result = buscar(entradas[k][1], nome_arquivo)
            buscado, result, qtddd = buscar(entradas[k][1], lista_arq_criados2)
            i = 0
            while i < len(buscado):
                print(f'{buscado[i]}'+ f'{ result[i] }'+ ' ' + f'{ entradas[k][1]}')
                i += 1
            print(f'{qtddd} arquivos encontrados')

        if entradas[k][0] == 'mostrar':
            #print(entradas[k][0])
            mostrado = mostrar(entradas[k][1])

        if entradas[k][0] == 'carregar':
            arq_criados += 1
            lista_arq_criados.append(f'{entradas[k][2]}'+ f' {admin[0]}')
            arq_velho, arq_novo = carregar(entradas[k][1], entradas[k][2]) 
            print(f'{entradas[k][1]} carregado como {entradas[k][2]}')

        if entradas[k][0] == 'comparar':
            lista_c, lista_b = comparar(entradas[k][1], entradas[k][2])
            #print(lista_c)
            
            if '<  ' in lista_c:
                    lista_c.pop(-1)
            for s in range(len(lista_c)):
                print(lista_c[s])
            print('---')
            for m in lista_b:
                print(m)

        '''if  '-t' in entradas[k]:
            for h in lista_arq_criados:
                print(h)
            print(f'{arq_criados} arquivos existentes')'''

        if entradas[k][0] == 'listar':
            if len(entradas[k]) == 2:
                for h in lista_arq_criados:
                    print(h)
                print(f'{arq_criados} arquivos existentes')
            else:
                new_lista_arq_criads = sorted(lista_arq_criados)
                for s in new_lista_arq_criads:
                    print(s)
                print(f'{arq_criados} arquivos existentes')

        if entradas[k][0] == 'terminar':
            print('até mais!')

    #print(entradas)
    #new_lista_arq_criads = sorted(lista_arq_criados)
    #print(lista_arq_criados)
    #print(new_lista_arq_criads)
    #print(lista_arq_criados2)


main()