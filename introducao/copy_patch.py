import math

def time(taxas, bytes_restantes):
    soma_taxas = sum(taxas)
    media = (soma_taxas / 5)
    tempo_restante = round(bytes_restantes / media, 4)
    return math.ceil(tempo_restante)


def main():
    num_bytes = int(input())
    num_bytes_transmitidos = 0
    taxas = []
    num_loops = 0

    print('Transmitindo ' + str(num_bytes) + ' bytes...')

    while num_bytes_transmitidos < num_bytes:
        taxa = int(input())
        taxas.append(taxa)
        num_bytes_transmitidos += taxa
        num_loops += 1
        soma_taxas = sum(taxas)
        bytes_restantes = num_bytes - soma_taxas


        if soma_taxas == num_bytes:
            print("Tempo total: " + str(num_loops) + " segundos.")
            break

        if num_loops % 5 == 0:
            taxas_media = taxas[num_loops - 5:num_loops]
            soma_taxas_medias = sum(taxas_media)

            if soma_taxas_medias == 0:
                print("Tempo restante: pendente... ")

            else:
                sec = time(taxas_media, bytes_restantes)
                print("Tempo restante: " + str(sec) + " segundos.")


main()
