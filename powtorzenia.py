
def licznik_powtorzen():
    f = open(r'hiszpańskie słówka.txt', 'r', encoding="utf-8")
    lista=[]
    for line in f:
        hiszpanski, polski = line.split(" - ")
        lista.append(hiszpanski)
    dict = {x: lista.count(x) for x in lista if lista.count(x)>1}

    if dict=={}:
        print("brak powtórzeń")
    else:
        for i in dict: print(f"{i} - {dict[i]} powtórzeń")
    f.close()

licznik_powtorzen()
