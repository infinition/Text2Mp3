import os
import tkinter as tk
from tkinter import *
import subprocess as sp
import subprocess, shlex
from gtts import gTTS


master = tk.Tk()
master.title("P")
master.minsize(140, 140)
master.maxsize(140, 140)
master.config(background="black")
master.wm_attributes("-topmost", 1)


def returnEntryR2(arg=None):
    global current_resultR1
    result1 = myEntryR1.get()
    current_resultR1 = result1
    print(current_resultR1)
    tts = gTTS(text=result1, lang='fr')
    tts.save(result1 + ".mp3")
#os.system("start english.mp3")
    myEntryR1.delete(0,END)
    master.destroy()



    #Ajout du texte LOGIN
label_titleR1 = Label(master, text="Mot à enregistrer", font="Courrier, 8", bg="black", fg='white')
label_titleR1.pack()
# Zone de saisie LOGIN
myEntryR1 = Entry(master, width=20)
myEntryR1.focus()
myEntryR1.bind("<Return>",returnEntryR2)
myEntryR1.pack()


# Bouton valider 
enterEntryR2 = Button(master, text= "Valider", command=returnEntryR2)
enterEntryR2.pack(fill=X)

master.mainloop()