def lesma():
    les_num = int(input())

    aux_array = []
    for i in range(les_num):
        num = int(input())
        aux_array.append(num)

    array_um = []
    array_dois = []
    array_tres = []

    for i in aux_array:
        if(i < 10):
            array_um.append(i)
        if(i >= 10 and i < 20):
            array_dois.append(i)
        if(i > 20):
            array_tres.append(i)
    
    array_um.sort(reverse=True)
    array_dois.sort(reverse=True)
    array_tres.sort(reverse=True)

    print(array_um)
    resultado = []
    if array_um:
        resultado.append(array_um[0])
    else: 
        resultado.append(0)

    if array_dois:
        resultado.append(array_dois[0])
    else:
        resultado.append(0)

    
    if array_tres:
        resultado.append(array_tres[0])
    else:
        resultado.append(0)

    print(resultado)

lesma()