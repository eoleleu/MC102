from sequencias import * 

def main():
    n = int(input())
    sequencia_genoma = list(input())
    genoma_variante = list(input())
    
    dif = diferencas(sequencia_genoma, genoma_variante, n)
    
    
    #for i in range(int(len(dif)/4)):
    #    print(f'Diferença {(i+1)}:')
    #    print(f'   Posição: {dif[i*4]}')
    #    print(f'Referência: {"".join(dif[i*4+1])}')
    #    print(f'  Variante: {"".join(dif[i*4+2])}')
    #    print(f' Distância: {dif2[i*4+3]}')
    #
    i = 1
    for ind in dif:
        print(f"Diferença {i}:")
        print(f"   Posição: {ind}")
        referencia =  "".join(sequencia_genoma[ind:ind+n])
        variante = "".join(genoma_variante[ind:ind+n])
        distancia = distancia_hamming(referencia, variante)
        print(f"Referência: {referencia}")
        print(f"  Variante: {variante}")
        print(f"Distância: {distancia}\n")
        i += 1



    
    

main()