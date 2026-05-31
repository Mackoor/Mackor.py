from . import gracz as g

from . import enemi as e

from . import umiejetnosci as u

from . import tekst as t

from random import randint

import math

import time

import os






def attack(gracz:dict,enemy):
    cos = randint(0,100)
    if cos < 50:
        t.tekst_do_bitki_goblin()
        while True:
            if g.gracz["Hp"] >= 0:
                if g.gracz["Hp"] <= 0:
                    print("zginołes")
                    break
                if e.enemy[0]["Hp"] <= 0:
                    e.reset_enemy(enemy)
                    t.wygrałes(gracz,enemy)
                    break
            t.tekst_do_ruchów()
            g.HP_ITD(gracz,enemy)
            inp = input("Twój ruch: ")
            if inp == "a":
                time.sleep(1)
                os.system("cls") 
                while True:
                    t.lista_attaków()
                    inp = input("Twój ruch: ")
                    if inp == "1":
                        u.slach(gracz,enemy)
                        time.sleep(1) 
                        break
                    if inp == "2":
                        u.heavy_slach(gracz,enemy)
                        time.sleep(1)
                        break
                    if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
            elif inp == "p":
                u.Potki(gracz)
            elif inp == "o":
                u.odpoczynek(gracz,enemy)
            elif inp == "e":
                czy = randint(0,20)
                if czy < 10 :        
                    g.gracz["Hp"] -= e.enemy[0]["Dmg"]
                    print(f"\t Podczas pruby ucieczki goblin cie złapał starciłes {e.enemy[0]["Dmg"]}Hp")
                    print("\t Nie udana ucieczka")
                elif czy >= 10:
                    print("\t udana ucieczka")
                    break
    elif cos >= 50:
        while True:
            t.tekst_do_bitki_wilk()
            if g.gracz["Hp"] >= 0:
                if g.gracz["Hp"] <= 0:
                    print("zginołes")
                    break
                if e.enemy[1]["Hp"] <= 0:
                    e.reset_enemy(enemy)
                    t.wygrałes(gracz,enemy)
                    break
            t.tekst_do_ruchów()
            g.HP_ITD(gracz,enemy)
            inp = input("Twój ruch: ")
            if inp == "a":
                time.sleep(1)
                os.system("cls") 
                while True:
                    t.lista_attaków()
                    inp = input("Twój ruch: ")
                    if inp == "1":
                        u.slach(gracz,enemy)
                        time.sleep(1) 
                        break
                    if inp == "2":
                        u.heavy_slach(gracz,enemy)
                        time.sleep(1)
                        break
                    if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
            elif inp == "p":
                u.Potki(gracz)
            elif inp == "o":
                u.odpoczynek(gracz,enemy)
            elif inp == "e":
                czy = randint(0,20)
                if czy < 10 :        
                    g.gracz["Hp"] -= e.enemy[1]["Dmg"]
                    print(f"\t Podczas pruby ucieczki wilk cie złapał starciłes {e.enemy[1]["Dmg"]}Hp")
                    print("\t Nie udana ucieczka")
                elif czy >= 10:
                    print("\t udana ucieczka")
                    break







# def tekst_do_bitki():
   # print(f"\t {"="*40} \n \t WALKA ROZPOCZYNA SIĘ \n \t {"="*40} \n \n \t Wchodzisz głębiej w las. Drzewa robią się \n \t gęstsze, a światło znika, jakby ktoś \n \t powoli wyłączał grafikę w ustawieniach. \n \n \t Nagle słyszysz szelest. \n \n \t Z krzaków wyskakuje goblin. \n \t Ma krzywy uśmiech, patyk zamiast broni \n \t i minę człowieka, który absolutnie \n \t nie planuje dziś być rozsądny. \n  \n \t Goblin: \n \t ""REEE!!"" \n \n \t Nie brzmi to jak argument do negocjacji.")








def miasto_reszta(gracz):
    if inp == "1":
        while True:
            os.system("cls")
            t.kuznia()
            inp = input("\t Co tobisz: ")
            if inp == "1":
                if gracz["Gold"] >= 20:
                    gracz["Gold"] -= 20
                    print("\t Kupiłes miecz \n \t +5 - Dmg")
                    gracz["Dmg"] += 5
                elif gracz["Gold"] <= 20:
                    print("\f jestes biedakiem nie stac cie na mieczyk")
            elif inp == "2":
                if gracz["Gold"] >= 18:
                    gracz["Gold"] -= 18
                    print("\t Kupiłes zbrojke \n \t +20 - Max_Hp")
                    gracz["Max_Hp"] += 20
                    gracz["Hp"] += 20
                elif gracz["Gold"] <= 18:
                    print("\f jestes biedakiem nie stac cie na zbrojke")
            elif inp == "3":
                kowal_sklep(gracz)
            elif inp == "4":
                print("Wychodzisz od kowala.")
                break
    elif inp == "2":
        while True:
            os.system("cls")
            t.alchemik()
            inp = input("\t Co tobisz: ")
            if inp == "1":
                sklep_alchemika(gracz)
            elif inp == "2":
                if gracz["Gold"] >= 28:
                    gracz["Gold"] -= 28
                    print("\t Kupiłes zbrojke \n \t +20 - Max_Hp")
                    gracz["Max_Stamina"] += 50
                    gracz["Stamina"] += 50
                elif gracz["Gold"] <= 28:
                    print("\f jestes biedakiem nie stac cie na zbrojke")
            elif inp == "3":
                print("Wychodzisz od Alchemika.")
                break
    elif inp == "3":
        while True:
            t.kupca()
            if inp == "1":
                kupiec_skel(gracz)
            elif inp == "2":
                print("\t Wychodzisz od kupca")
                break
    elif inp == "4":
        while True:
            t.karczma()
            os.system("cls")
            if inp == "1":
                print("\t Przyciaołes sobie komara kturego berdzao potzrebowąłes")
                gracz["Stamina"] = gracz["Max_Stamina"]
            elif inp == "2":
                print("\t wychodisz z karczmy")
                break








def dungeona(gracz:dict,enemy):
    t.dungeon_dalej()
    inp = input("\t co robisz: ")
    if inp == "1":
        cos = randint(0,100)
        if cos < 50:
            t.tekst_do_bitki_goblin()
            while True:
                if g.gracz["Hp"] >= 0:
                    if g.gracz["Hp"] <= 0:
                        print("zginołes")
                        break
                    if e.enemy[2]["Hp"] <= 0:
                        e.reset_enemy(enemy)
                        t.wygrałes(gracz,enemy)
                        break
                t.tekst_do_ruchów()
                g.HP_ITD(gracz,enemy)
                inp = input("Twój ruch: ")
                if inp == "a":
                    time.sleep(1)
                    os.system("cls") 
                    while True:
                        t.lista_attaków()
                        inp = input("Twój ruch: ")
                        if inp == "1":
                            u.slach(gracz,enemy)
                            time.sleep(1) 
                            break
                        if inp == "2":
                            u.heavy_slach(gracz,enemy)
                            time.sleep(1)
                            break
                        if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
                elif inp == "p":
                    u.Potki(gracz)
                elif inp == "o":
                    u.odpoczynek(gracz,enemy)
                elif inp == "e":
                    czy = randint(0,20)
                    if czy < 10 :        
                        g.gracz["Hp"] -= e.enemy[2]["Dmg"]
                        print(f"\t Podczas pruby ucieczki goblin cie złapał starciłes {e.enemy[2]["Dmg"]}Hp")
                        print("\t Nie udana ucieczka")
                    elif czy >= 10:
                        print("\t udana ucieczka")
                        break
        elif cos >= 50:
            while True:
                t.tekst_do_bitki_wilk()
                if g.gracz["Hp"] >= 0:
                    if g.gracz["Hp"] <= 0:
                        print("zginołes")
                        break
                    if e.enemy[3]["Hp"] <= 0:
                        e.reset_enemy(enemy)
                        t.wygrałes(gracz,enemy)
                        break
                t.tekst_do_ruchów()
                g.HP_ITD(gracz,enemy)
                inp = input("Twój ruch: ")
                if inp == "a":
                    time.sleep(1)
                    os.system("cls") 
                    while True:
                        t.lista_attaków()
                        inp = input("Twój ruch: ")
                        if inp == "1":
                            u.slach(gracz,enemy)
                            time.sleep(1) 
                            break
                        if inp == "2":
                            u.heavy_slach(gracz,enemy)
                            time.sleep(1)
                            break
                        if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
                elif inp == "p":
                    u.Potki(gracz)
                elif inp == "o":
                    u.odpoczynek(gracz,enemy)
                elif inp == "e":
                    czy = randint(0,20)
                    if czy < 10 :        
                        g.gracz["Hp"] -= e.enemy[3]["Dmg"]
                        print(f"\t Podczas pruby ucieczki wilk cie złapał starciłes {e.enemy[3]["Dmg"]}Hp")
                        print("\t Nie udana ucieczka")
                    elif czy >= 10:
                        print("\t udana ucieczka")
                        break
    if inp == "1":
        cos = randint(0,100)
        if cos < 50:
            t.tekst_do_bitki_goblin()
            while True:
                if g.gracz["Hp"] >= 0:
                    if g.gracz["Hp"] <= 0:
                        print("zginołes")
                        break
                    if e.enemy[3]["Hp"] <= 0:
                        e.reset_enemy(enemy)
                        t.wygrałes(gracz,enemy)
                        break
                t.tekst_do_ruchów()
                g.HP_ITD(gracz,enemy)
                inp = input("Twój ruch: ")
                if inp == "a":
                    time.sleep(1)
                    os.system("cls") 
                    while True:
                        t.lista_attaków()
                        inp = input("Twój ruch: ")
                        if inp == "1":
                            u.slach(gracz,enemy)
                            time.sleep(1) 
                            break
                        if inp == "2":
                            u.heavy_slach(gracz,enemy)
                            time.sleep(1)
                            break
                        if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
                elif inp == "p":
                    u.Potki(gracz)
                elif inp == "o":
                    u.odpoczynek(gracz,enemy)
                elif inp == "e":
                    czy = randint(0,20)
                    if czy < 10 :        
                        g.gracz["Hp"] -= e.enemy[3]["Dmg"]
                        print(f"\t Podczas pruby ucieczki goblin cie złapał starciłes {e.enemy[2]["Dmg"]}Hp")
                        print("\t Nie udana ucieczka")
                    elif czy >= 10:
                        print("\t udana ucieczka")
                        break
        elif cos >= 50:
            while True:
                t.tekst_do_bitki_wilk()
                if g.gracz["Hp"] >= 0:
                    if g.gracz["Hp"] <= 0:
                        print("zginołes")
                        break
                    if e.enemy[2]["Hp"] <= 0:
                        e.reset_enemy(enemy)
                        t.wygrałes(gracz,enemy)
                        break
                t.tekst_do_ruchów()
                g.HP_ITD(gracz,enemy)
                inp = input("Twój ruch: ")
                if inp == "a":
                    time.sleep(1)
                    os.system("cls") 
                    while True:
                        t.lista_attaków()
                        inp = input("Twój ruch: ")
                        if inp == "1":
                            u.slach(gracz,enemy)
                            time.sleep(1) 
                            break
                        if inp == "2":
                            u.heavy_slach(gracz,enemy)
                            time.sleep(1)
                            break
                        if inp == "3":
                            u.kopniecie(gracz,enemy)
                            time.sleep(1)
                            break
                elif inp == "p":
                    u.Potki(gracz)
                elif inp == "o":
                    u.odpoczynek(gracz,enemy)
                elif inp == "e":
                    czy = randint(0,20)
                    if czy < 10 :        
                        g.gracz["Hp"] -= e.enemy[2]["Dmg"]
                        print(f"\t Podczas pruby ucieczki wilk cie złapał starciłes {e.enemy[3]["Dmg"]}Hp")
                        print("\t Nie udana ucieczka")
                    elif czy >= 10:
                        print("\t udana ucieczka")
                        break








def kupiec_skel(gracz):
    print("\t Kupiec patrzy na twoje trofea.")
    print("\t Co chcesz sprzedać?\n")

    print("\t 1 - Ucho wilka (10 gold)")
    print("\t 2 - Kieł wilka (15 gold)")
    print("\t 3 - Futro wilka (20 gold)")
    print("\t 4 - Kieł goblina (12 gold)")
    print("\t 5 - Ucho goblina (8 gold)")
    print("\t 6 - Serce nieumarłego (40 gold)")
    print("\t 7 - Palec (5 gold)")
    print("\t 8 - Kość (7 gold)")
    print("\t 9 - Wyjdź")

    inp = input("\t Co chzesz sprzedac")

    if inp == "1":
        if "Ucho wilka" in gracz["EQ"]:
            gracz["EQ"].remove("ucho_wilka")
            gracz["Gold"] += 10
            print("\t Sprzedano Ucho wilka.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "2":
        if "Kieł wilka" in gracz["EQ"]:
            gracz["EQ"].remove("kieł_wilka")
            gracz["Gold"] += 15
            print("\t Sprzedano Kieł wilka.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "3":
        if "Futro wilka" in gracz["EQ"]:
            gracz["EQ"].remove("futro_wilka")
            gracz["Gold"] += 20
            print("\t Sprzedano Futro wilka.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "4":
        if "Kieł goblina" in gracz["EQ"]:
            gracz["EQ"].remove("kieł_goblina")
            gracz["Gold"] += 12
            print("\t Sprzedano Kieł goblina.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "5":
        if "Ucho goblina" in gracz["EQ"]:
            gracz["EQ"].remove("ucho_goblina")
            gracz["Gold"] += 8
            print("\t Sprzedano Ucho goblina.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "6":
        if "Serce nieumarłego" in gracz["EQ"]:
            gracz["EQ"].remove("serce_nieumarłego")
            gracz["Gold"] += 40
            print("\t Sprzedano Serce nieumarłego.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "7":
        if "Palec" in gracz["EQ"]:
            gracz["EQ"].remove("palec")
            gracz["Gold"] += 5
            print("\t Sprzedano Palec.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "8":
        if "Kość" in gracz["EQ"]:
            gracz["EQ"].remove("Kosc")
            gracz["Gold"] += 7
            print("\t Sprzedano Kość.")
        else:
            print("\t Nie masz tego przedmiotu.")

    elif inp == "9":
        print("Wychodzisz od kupca.")







def kowal_sklep(gracz):
    print("\t Kowal patrzy na twój ekwipunek.")
    print("\t Co chcesz sprzedać?")
    print("\t 1 - Miecz \n \t 2 - Łuk \n \t 3 - Wyjdź")
    inp = ("\t Co chzesz sprzedac: ")
    if inp == "1":
        if "Miecz" in gracz["EQ"]:
            gracz["EQ"].remove("Miecz")
            gracz["Gold"] += 30
            print("Sprzedano Miecz za 30 golda.")
        else:
            print("Nie masz Miecza.")

    elif inp == "2":
        if "Łuk" in gracz["EQ"]:
            gracz["EQ"].remove("Łuk")
            gracz["Gold"] += 20
            print("Sprzedano Łuk za 20 golda.")
        else:
            print("Nie masz Łuku.")

    elif inp == "3":
        print("Wychodzisz od kowala.")

def sklep_alchemika(gracz):
    print("\t Alchemik pokazuje swoje mikstury.")
    print("\t 1 - Potion leczenia (20 gold)")
    print("\t 2 - Wyjście")
    inp = ("\t co tam chczesz")
    if inp == "1":
        if gracz["Gold"] >= 20:
            gracz["Gold"] -= 20
            gracz["EQ"].append("Hp_Potion")
            print("Kupiono Potion leczenia!")
        else:
            print("Za mało golda.")

    elif inp == "2":
        print("Wychodzisz od alchemika.")