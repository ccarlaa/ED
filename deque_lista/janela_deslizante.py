tamanhoLista = int(input())
lista = input().split()
tamanhoJanela = int(input())
inteiros = list(map(int, lista))

index = 0

for index, item in enumerate(inteiros):
    if index + tamanhoJanela > tamanhoLista:
        break

    valorMaior = inteiros[index:tamanhoJanela+index]  # Converter para inteiros
    valorMaior.sort()
    valorMaior.reverse()
    
    print(valorMaior[0], end='  ')  # Agora não dará erro
