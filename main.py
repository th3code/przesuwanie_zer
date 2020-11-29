lista = [0, 1, 5, 0, 2, 6, 3, 0, 7]

def pobierzIndexy(l):
    licznik=0
    a = []
    for x in l:
            if x == 0:
                a.append(licznik)
            licznik += 1
    return(a)

listaIndexow = pobierzIndexy(lista)
print(lista)
print(len(lista))
print(listaIndexow)
print(len(listaIndexow))

