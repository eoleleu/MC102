from sequencias import * 


def main():
    sequencia = input().split()

    sequencia_nova = []

    for a in sequencia:
        b = list(a)
        sequencia_nova.extend(b)

    n = int(input())

    lista = []

    for _ in range(n):
        sequencias_candidatas = input().split()
        lista.extend(sequencias_candidatas)

    canditado_min, d = minima_distancia(sequencia[0], lista)

    print(f"Sequência mais próxima: {canditado_min} ")
    print(f"Distância de Hamming: {d} ")


main()
