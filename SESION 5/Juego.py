from tkinter import *
import random

ws = Tk()
ws.title('Juego en Phyton')
ws.geometry('600x400')
ws.config(bg='#5671A6')

ranNum = random.randint(0, 10)
chance = 5
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0:
        if usr_ip == ranNum:
            msg = f'Has Ganado! {ranNum} es la respuesta correcta.'
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} es mas grande. Tu tienes {chance} intentos.'
        elif usr_ip < ranNum:
            chance -= 1
            msg = f'{usr_ip} es mas pequeño. Tu tienes {chance} intentos.'
        else:
            msg = 'Algo ha ocurrido!'
    else:
        msg = f'Has Perdido! tu tienes {chance} Intentos.'

    disp.set(msg)


Label(
    ws,
    text="Adivina el Numero",
    font=('sans-serif', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    ws,
    text="Presiona aqui",
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))


ws.mainloop()