def frequencia(palavra):
    maior_freq = 0
    auxnum = 0
    auxcaractere = ""
    for x in palavra:
        auxnum = 0
        for y in palavra:
            if x == y:
                auxnum += 1
        if maior_freq < auxnum:
            auxcaractere = x
            maior_freq = auxnum
    return auxcaractere
