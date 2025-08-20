import random
import tkinter as tk
import zmienne as z

def przygotuj():
    f = open(r'hiszpańskie słówka 2.txt', 'r', encoding="utf-8")
    slowka=[]
    for line in f:
        slowka.append(line)
    slowka[-1]+='x'
    random.shuffle(slowka)
    if len(slowka)>500:
        slowka=slowka[:500]
    for i in slowka:
        hiszpanski, polski = i.split(' - ')
        polski=polski[:-1]
        z.slownik[polski]=hiszpanski
        z.lista.append(polski)

def sprawdz(box, slownik, lista, pytanie, pozostale):
    tekst=box.get("1.0", tk.END)
    tekst=tekst[:-2]
    box.delete('1.0', tk.END)
    if pytanie.cget('text') in slownik:
        poprawne = slownik[pytanie.cget('text')]
        if tekst==poprawne:
            lista.remove(pytanie.cget('text'))
            pytanie.config(text='Dobrze', fg='green')
        else:
            pytanie.config(text=f'Źle! Poprawno odpowiedź: {poprawne}', fg='red')
    elif lista:
        wybierz(lista, pytanie)
    else:
        pytanie.config(text='Wszystkie słówka nauczone!', fg='green')
    pozostale.config(text=f'Pozostało słówek: {len(lista)}')

def wybierz(lista, pytanie):
    x=random.choice(lista)
    pytanie.config(text=x, fg='black')

