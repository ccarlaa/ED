def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero = 24
print(f"Os divisores de {numero} são:", encontrar_divisores(numero))