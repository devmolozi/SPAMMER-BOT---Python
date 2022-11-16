import time
from math import atan, pi, sqrt
from tkinter import *
import pyautogui as spam

#-------- INICIO FUNCAO --------#

def onmsg():

    limite = (quantidade.get())
    mensagem1 = (mensagem.get())
    quantidade.delete(0, END)
    mensagem.delete(0, END)

    time.sleep(2)

    i = 0

    while i < int(limite):

        spam.typewrite(mensagem1)
        spam.press("enter")

        i += 1

#-------- FIM FUNCAO --------#

 
#-------- INICIO APP --------#

app = Tk()
app.title("SPAMMER BOT")
app.geometry("400x400+0+0")
app.configure(background="#2a007c")


txt = Label (app, text="S P A M M E R  B O T", font=("Arial",15), fg="white", bg="#2a007c")
txt.place(x=100,y=50)

txt1 = Label(app, text="Número de mensagens", font=("Arial",11), fg="white", bg="#2a007c")
txt1.place(x=70,y=105)

quantidade = Entry(app, font=("Arial",12), width=30, fg="white", bg="#3f098f",highlightbackground = "#7c23c6", highlightthickness = 0.5, bd=0)
quantidade.place(x=70, y=135)

txt2 = Label(app, text="Digite a mensagem", font=("Arial",11), fg="white", bg="#2a007c")
txt2.place(x=70,y=170)

mensagem = Entry(app,font=("Arial",12), width=30, fg="white", bg="#3f098f",highlightbackground = "#7c23c6", highlightthickness = 0.5, bd=0)
mensagem.place(x=70, y=200)

bt = Button(app, font=("Arial",12),width=20, text="Start Spammer BOT", fg="white", bg="#3f098f" , command=onmsg,highlightbackground = "#7c23c6", highlightthickness = 2, bd=0)
bt.place(x=110, y=260)


txt3 = Label(app, text="Criado por @molozi_", fg="white", bg="#2a007c")
txt3.place(x=145,y=350)


app.mainloop()

#-------- FIM APP --------#









