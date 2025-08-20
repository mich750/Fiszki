import tkinter as tk
import funkcje as f
import tworzenie_menu as m
import zmienne as z

root=tk.Tk()
root.attributes('-fullscreen', True)

slowko=tk.Label(root, text='aaa', font=('Arial', 40), anchor='center', justify='center', width=45)
slowko.place(x=70, y=150)
tekst=tk.Text(root, font=('Arial', 40), width=35, height=1)
tekst.place(x=250, y=280)
pozostale=tk.Label(root, text='', font=('Arial', 40), anchor='center', width=45)
pozostale.place(x=70, y=500)

f.przygotuj()

menu_glowne=tk.Menu(root)
root.config(menu=menu_glowne)
menu=tk.Menu(menu_glowne, tearoff=0)
menu_glowne.add_cascade(label='Menu', menu=menu)
menu.add_command(label="Ustawienia", command=lambda: m.ustawienia(slowko, pozostale))
menu.add_command(label='Wyjdź (Esc)', command=lambda: root.destroy())

f.wybierz(z.lista, slowko)

root.bind('<Escape>', lambda x: root.destroy())
root.bind('<Return>', lambda x: f.sprawdz(tekst, z.slownik, z.lista, slowko, pozostale))

root.mainloop()