def triangulo(n):
    if n == 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        linha_ant = pascal[i - 1]
        nova_fileira = [1]

        for j in range(1, i):
            novo_num = linha_ant[j - 1] + linha_ant[j]
            nova_fileira.append(novo_num)

        novo_num = 1
        nova_fileira.append(novo_num)
        pascal.append(nova_fileira)

    return pascal

