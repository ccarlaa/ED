class ListaDinamica:
    def __init__(self):
        self.lista = []

    def inserir_inicio(self, valor):
        self.lista.insert(0, valor)

    def inserir_final(self, valor):
        self.lista.append(valor)

    def remover_inicio(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return

    def remover_final(self):
        if self.lista:
            return self.lista.pop()
        else:
            return

    def imprimir(self):
        for i in self.lista:
            print(i)


def processar_comandos():
    lista = ListaDinamica()
    while True:
        entrada = input()
        entrada = entrada.split()

        operacao = entrada[0].upper()

        if operacao == 'X':
            lista.imprimir()
            break

        if len(entrada) != 2:
            if operacao == 'P':
                valor_removido = lista.remover_final()
                if valor_removido is not None:
                    print(valor_removido)
            if operacao == 'D':
                valor_removido = lista.remover_inicio()
                if valor_removido is not None:
                    print(valor_removido)
            continue

        valor = int(entrada[1])

        if operacao == 'I':
            lista.inserir_inicio(valor)
        elif operacao == 'F':
            lista.inserir_final(valor)
    

processar_comandos()
