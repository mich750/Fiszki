def kasowanie():
    f = open(r'hiszpańskie słówka 2.txt', 'r', encoding="utf-8")
    lista=f.readlines()
    lista=list(dict.fromkeys(lista))
    f.close()
    f = open(r'hiszpańskie słówka 2.txt', 'w', encoding="utf-8")
    for line in lista:
        if line!='\n': f.write(line)
    f.close()

kasowanie()

