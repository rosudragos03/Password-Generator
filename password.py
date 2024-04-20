import random
import string
import tkinter as tk

def generare_parola(lungime):
    caractere = string.ascii_letters + string.digits + string.punctuation
    parola = ''.join(random.choice(caractere) for _ in range(lungime))
    return parola

def generare_parola_interfata():
    lungime_parola = int(entry_lungime.get())
    if lungime_parola < 6:
        label_rezultat.config(text="Lungimea parolei trebuie să fie de cel puțin 6 caractere.")
    else:
        parola_generata = generare_parola(lungime_parola)
        label_rezultat.config(text="Parola generată: " + parola_generata)

root = tk.Tk()
root.title("Generator de parole")

label_lungime = tk.Label(root, text="Introduceți lungimea parolei dorite: ")
label_lungime.pack()

entry_lungime = tk.Entry(root)
entry_lungime.pack()

button_generare = tk.Button(root, text="Generare Parola", command=generare_parola_interfata)
button_generare.pack()

label_rezultat = tk.Label(root, text="")
label_rezultat.pack()

root.mainloop()
