from funkcje import rozgrywka as r
from funkcje import enemi as e
from funkcje import gracz as g
from funkcje import umiejetnosci as u
from funkcje import tekst as t
import os
import time

t.tekst_poczatkowy()
def main():
    while True:
        t.teks_z_miejscami()
        inp = input("\t Twój wybór: ")
        if inp == "a":
            os.system("cls")
            r.attack(g.gracz,e.enemy[0],e.enemy[1])
        elif inp == "g":
            os.system("cls")
            g.gracza(g.gracz)
            time.sleep(2.5)
        elif inp == "q":
            os.system("cls")
            g.EQ(g.gracz)
            time.sleep(2.5)
        elif inp == "i":
            os.system("cls")
            t.miasto
            t.misato_wybór
            inp = input("\t Twój wybór: ")
        elif inp == "P":
            os.system("cls")
            u.Potki(g.gracz)
            os.system("cls")
        elif inp == "d":
            t.dungeon()
            while True:
                inp = ("\t co robisz")
                if inp == "1":
                    r.dungeona(g.gracz,e.enemy[2],e.enemy[3])
                elif inp == "2":
                    break
        elif inp == "e":
            os.system("cls")
            break




main()


