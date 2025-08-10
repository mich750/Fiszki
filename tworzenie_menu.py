import tkinter as tk
import zmienne as z
import funkcje

def zamien():
    for i in range(len(z.lista)):
        z.lista[i]=z.slownik[z.lista[i]]
    z.slownik= {i:j for (i,j) in zip(list(z.slownik.values()), list(z.slownik))}

def ograniczenie(tekst):
    if tekst == "": return True
    elif tekst.isdigit():
        if int(tekst)>500: return False
        else: return True
    else: return False

def potwierdz(textbox, okno, j_odp, pytanie, pozostale):
    if z.jezyk!=j_odp:
        zamien()
        funkcje.wybierz(z.lista, pytanie)
    if textbox.get()=='': liczba_slow=500
    else: liczba_slow=int(textbox.get())
    if len(z.lista)>liczba_slow:
        z.lista=z.lista[:liczba_slow]
        funkcje.wybierz(z.lista, pytanie)
    okno.destroy()
    pozostale.config(text=f'Pozostało słówek: {len(z.lista)}')

def ustawienia(pytanie, pozostale):
    okno=tk.Toplevel()
    okno.geometry('500x450+500+150')
    label1=tk.Label(okno, text="Podaj liczbę słów do nauki: (max 500)", font=('Arial', 20))

    walidacja = okno.register(ograniczenie)
    tekst=tk.Entry(okno, validate='key', validatecommand=(walidacja, '%P'), font=('Arial', 20))

    label2=tk.Label(okno, text="Język odpowiedzi:", font=('Arial', 20))

    var=tk.StringVar(value='pl')
    radiobutton1=tk.Radiobutton(okno, text='polski', value='pl', variable=var, font=('Arial', 20))
    radiobutton2=tk.Radiobutton(okno, text='hiszpański', value='hisz', variable=var, font=('Arial', 20))

    przycisk1=tk.Button(okno, text="Zastosuj", font=('Arial', 20), command=lambda: potwierdz(tekst, okno, var.get(), pytanie, pozostale))
    przycisk2=tk.Button(okno, text='Anuluj', font=('Arial', 20), command=lambda: okno.destroy())

    label1.grid(row=0, column=0, columnspan=2, padx=30, pady=30)
    tekst.grid(row=1, column=0, columnspan=2, padx=30, pady=30)
    label2.grid(row=2, column=0, columnspan=2)
    radiobutton1.grid(row=3, column=0, columnspan=2)
    radiobutton2.grid(row=4, column=0, columnspan=2)
    przycisk1.grid(row=5, column=0)
    przycisk2.grid(row=5, column=1)

    okno.mainloop()