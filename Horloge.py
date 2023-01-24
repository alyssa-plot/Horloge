from tkinter import *
from time import strftime
import time

master = Tk()
master.title('Horloge')
master.geometry('250x50')

master = Label(master, font=('', 20, 'bold'), bg='#7ca583')
master.pack()

def alarme():
    reglage_alarme = "%H:%M:%S" #tu définis l'heure de ton alarme

    if strftime('%H:%M:%S') == reglage_alarme:
        print("DRINGDRINDRINGDRING") #ça va spammer jusqu'à que tu décides de l'arrêter
        master.after(100, alarme)


def afficher_heure():
    master.config(text=strftime('%H:%M:%S'))
    master.after(100,afficher_heure)
    alarme()

#Pour choisir ton heure, il te suffira de décommenter ce paragraphe ci-dessous:
# def printe():
#    h = int(input('heures : '))
#    min = int(input('min : '))
#    sec = int(input('sec : '))
#    while h < 24:
#        while min < 60:
#            while sec < 60:
#                print(h,':',min,':',sec)
#                time.sleep(1)
#                sec=sec+1
#            sec=0
#            min=min+1
#        h=h+1
#        min=0
# printe()

afficher_heure()
master.mainloop()
