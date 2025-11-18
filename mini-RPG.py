from random import randint
import os
import time
# hp atak mana gold
hero = [100,10,1,100,0]
materiały = [0,0,0,0,0,0,0,0,0,0,0]
Eq = [0,0,0,0]
print("\tbudzisz sie na ścieżce")
print("\tco robisz?")
time.sleep(2)
while hero[0] > 0:
    if hero[4] < 0:
        hero[4] == 0
    goblin = [randint(10,75),randint(10,20),randint(0,0),randint(10,60),1,randint(1,10),randint(1,2)]
    slime = [randint(50,200),randint(10,60),randint(0,0),randint(10,20),2,randint(1,6),]
    goblinking =[randint(250,500),randint(126,260),randint(0,0),randint(100,800),1]
    slimeking = [randint(300,700),randint(130,320),randint(0,0),randint(100,500),1]
    kwiat = [randint(5,15),randint(2,5),randint(0,0),randint(1,10),randint(1,16)]
    zioła = [randint(5,15),randint(2,5),randint(0,0),randint(1,10),randint(1,24)]
    grzyby = [randint(5,15),randint(2,5),randint(0,0),randint(1,10),randint(1,8)]
    print("""\ta - idz do lasu \n \tb - idz do miasta \n \tz - zobacz-ekwipunek \n \tc - nic nie rób""")
    print(f"\t~~HERO~~: ({hero[0]}) hp: ({hero[1]}) atak: ({hero[2]}) mana: ({hero[3]}) gold: ({hero[4]}) obrona:")
    print("==="*27)
    inp = input("co robisz: ").lower()
    print("==="*27)
    if inp == "a":
        print("wszedłes do lasu")
        while True:
            if hero[0] < 0:
                print("UMARLES")
                break
            print("\tp - pola \n \tg - głebiej w las \n \td - dungeon \n \tw - wracasz")
            print("==="*27)
            inp = input("gdzie idzesz: ")
            print("==="*27)
            if inp == "w":
                print("wraczasz przed wrota miasta")
                print("==="*27)
                time.sleep(2)
                break
            elif inp == "d":
                while True:
                    print("\ta - kopac minerały \n \tb - iść dalej w dungeona \n \tw - wracasz")
                    print("==="*27)
                    inp = input("gdzie idzesz: ")
                    print("==="*27)
                    if inp == "w":
                        print("wychodzisz z dungeona")
                        print("==="*27)
                        time.sleep(2)
                        break
                    elif inp == "a":
                        if Eq[2] <= 0:
                            print("Nie masz kilofa")
                        elif Eq[2] > 0:
                            minerały = [randint(1,10)]
                            Eq[2] -= 1
                            materiały[1] += minerały[0]
                            print(f"wykopałes {minerały[0]}")
                            print("straciełs jedno uzycie kilofa")
                            time.sleep(2)
                            break
                    elif inp == "b":
                        while True:
                            print("\ta - bijesz sie z slajmami \n \tb - boss room \n \tw - wracasz")
                            print("==="*27)
                            inp = input("gdzie idzesz: ")
                            print("==="*27)
                            if inp == "w":
                                print("wraczasz")
                                print("==="*27)
                                time.sleep(2)
                                break
                            elif inp == "b":
                                boss = [randint(1,20)]
                                if boss[0] <= 10:
                                    print("SPOTKAŁES GOBLINKINGA!!!")
                                    while True:
                                        if hero[0] < 0:
                                            print("UMARLES")
                                            break
                                        elif goblinking[4] == 0:
                                            print("Nie ma juz goblinkinga")
                                            time.sleep(2)
                                            break
                                        elif goblinking[0] < 0:
                                            print(f"WOW! Zloto! {goblinking[3]}")
                                            hero[3] += goblinking[3]
                                            print(f"WOW! boss-core! {goblinking[4]}")
                                            materiały[7] += goblinking[4]
                                            goblinking[4] -= goblinking[4]
                                            hero[4] -= 1
                                            break
                                        print(f"\tGoblinking hp {goblinking[0]} atak {goblinking[1]} ")
                                        print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                                        print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                                        inp = input("co robisz: ").lower()
                                        if inp == "a":
                                            if hero[4] >= 1:
                                                goblinking[0] -= hero[1]
                                                hero[4] -= 1
                                            elif hero[4] == 0:
                                                goblinking[0] -= hero[1]
                                                hero[0] -= goblinking[1]
                                        elif inp == "e":
                                            print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                            inp = input("co bierzesz: ")
                                            if inp == "l":
                                                if Eq[0] == 0:
                                                    break
                                                elif Eq[0] >= 1:
                                                    Eq[0] -= 1
                                                    hero[0] += 50
                                                    print("smakuje jak zywiec jasne pełne")
                                            elif inp == "m":
                                                if Eq[1] == 0:
                                                    break
                                                elif Eq[1] >= 1:
                                                    Eq[1] -= 1
                                                    hero[2] += 50
                                                    print("smakuje jak Zubr jasne pełne")
                                        elif inp == "o":
                                            if hero[4] == 0:
                                                hero[4] += 1
                                            elif hero[4] == 1:
                                                hero[4] -= 1
                                                hero[0] -= goblinking[1]
                                                print("za długo trzymałes obrone goblinking znalazł słaby punkt")
                                                time.sleep(2)
                                        elif inp == "z":
                                            if Eq[3] == 0:
                                                print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                                hero[0] -= goblinking[1]
                                            elif Eq[2] < 25:
                                                print("nie masz wystarczajaco many")
                                            elif Eq[3] <= 1:
                                                print("FIER_BALL!!!")
                                                time.sleep(2)
                                                goblinking[0] -= 125
                                                hero[2] -= 25
                                        else:
                                            print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                            hero[0] -= goblinking[1]
                                        time.sleep(1)
                                        os.system('cls')
                                elif boss[0] >= 11:
                                    print("SPOTKAŁES SLIMEKINGA!!!")
                                    while True:
                                        if hero[0] < 0:
                                            print("UMARLES")
                                            break
                                        elif slimeking[4] == 0:
                                            print("Nie ma juz slimeking")
                                            time.sleep(2)
                                            break
                                        elif slimeking[0] < 0:
                                            print(f"WOW! Zloto! {slimeking[3]}")
                                            hero[3] += slimeking[3]
                                            print(f"WOW! boss-core! {slimeking[4]}")
                                            materiały[7] += slimeking[4]
                                            slimeking[4] -= slimeking[4]
                                            hero[4] -= 1
                                            break
                                        print(f"\tSlimeking hp {slimeking[0]} atak {slimeking[1]} ")
                                        print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                                        print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                                        inp = input("co robisz: ").lower()
                                        if inp == "a":
                                            if hero[4] >= 1:
                                                slimeking[0] -= hero[1]
                                                hero[4] -= 1
                                            elif hero[4] == 0:
                                                slimeking[0] -= hero[1]
                                                hero[0] -= slimeking[1]
                                        elif inp == "e":
                                            print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                            inp = input("co bierzesz: ")
                                            if inp == "l":
                                                if Eq[0] == 0:
                                                    break
                                                elif Eq[0] >= 1:
                                                    Eq[0] -= 1
                                                    hero[0] += 50
                                                    print("smakuje jak zywiec jasne pełne")
                                            elif inp == "m":
                                                if Eq[1] == 0:
                                                    break
                                                elif Eq[1] >= 1:
                                                    Eq[1] -= 1
                                                    hero[2] += 50
                                                    print("smakuje jak Zubr jasne pełne")
                                        elif inp == "o":
                                            if hero[4] == 0:
                                                hero[4] += 1
                                            elif hero[4] == 1:
                                                hero[4] -= 1
                                                hero[0] -= slimeking[1]
                                                print("za długo trzymałes obrone slimeking znalazł słaby punkt")
                                                time.sleep(2)
                                        elif inp == "z":
                                            if Eq[3] == 0:
                                                print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                                hero[0] -= slimeking[1]
                                            elif Eq[2] < 25:
                                                print("nie masz wystarczajaco many")
                                            elif Eq[3] <= 1:
                                                print("FIER_BALL!!!")
                                                time.sleep(2)
                                                slimeking[0] -= 125
                                                hero[2] -= 25
                                        else:
                                            print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                            hero[0] -= slimeking[1]
                                        time.sleep(1)
                                        os.system('cls')
                            elif inp == "a":
                                while True:
                                    if hero[0] < 0:
                                        print("UMARLES")
                                        break
                                    elif slime[4] == 0:
                                        print("Nie ma wiecej Slajmów")
                                        time.sleep(2)
                                        break
                                    elif slime[0] < 0:
                                        print(f"WOW! Zloto! {slime[3]}")
                                        hero[3] += slime[3]
                                        print(f"WOW! Slime-core! {slime[4]}")
                                        materiały[6] += slime[4]
                                        print(f"WoW! Esencja-slajmów {slime[5]}")
                                        materiały[10] += slime[5]
                                        slime[4] -= slime[4]
                                        hero[4] -= 1
                                        break
                                    print(f"\tSlajmy hp {slime[0]} atak {slime[1]} ")
                                    print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                                    print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                                    inp = input("co robisz: ").lower()
                                    if inp == "a":
                                        if hero[4] >= 1:
                                            slime[0] -= hero[1]
                                            hero[4] -= 1
                                        elif hero[4] == 0:
                                            slime[0] -= hero[1]
                                            hero[0] -= slime[1]
                                    elif inp == "e":
                                        print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                        inp = input("co bierzesz: ")
                                        if inp == "l":
                                            if Eq[0] == 0:
                                                break
                                            elif Eq[0] >= 1:
                                                Eq[0] -= 1
                                                hero[0] += 50
                                                print("smakuje jak zywiec jasne pełne")
                                        elif inp == "m":
                                            if Eq[1] == 0:
                                                break
                                            elif Eq[1] >= 1:
                                                Eq[1] -= 1
                                                hero[2] += 50
                                                print("smakuje jak Zubr jasne pełne")
                                    elif inp == "o":
                                        if hero[4] == 0:
                                            hero[4] += 1
                                        elif hero[4] == 1:
                                            hero[4] -= 1
                                            hero[0] -= slime[1]
                                            print("za długo trzymałes obrone slime znalazł słaby punkt")
                                            time.sleep(2)
                                    elif inp == "z":
                                        if Eq[3] == 0:
                                            print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                            hero[0] -= slime[1]
                                        elif Eq[2] < 25:
                                            print("nie masz wystarczajaco many")
                                        elif Eq[3] <= 1:
                                            print("FIER_BALL!!!")
                                            time.sleep(2)
                                            slime[0] -= 125
                                            hero[2] -= 25
                                    else:
                                        print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                        hero[0] -= slime[1]
                                    time.sleep(1)
                                    os.system('cls')
            elif inp == "p":
                while True:
                    print("\ta - zbierasz kwiatki \n \tb - zbierasz zioła \n \tc - zbierasz grzyby \n \tw - wracasz")
                    print("==="*27)
                    inp = input("gdzie idzesz: ")
                    print("==="*27)
                    if inp == "w":
                        print("wraczasz na rozdrorze")
                        print("==="*27)
                        time.sleep(2)
                        break
                    elif inp == "a":
                        while True:
                            if hero[0] < 0:
                                print("UMARLES")
                                break
                            elif kwiat[4] == 0:
                                print("Nie ma wiecej kwiatów")
                                time.sleep(2)
                                break
                            elif kwiat[0] < 0:
                                print(f"WOW! Zloto! {kwiat[3]}")
                                hero[3] += kwiat[3]
                                print(f"WOW! Kwiatki! {kwiat[4]}")
                                materiały[3] += kwiat[4]
                                kwiat[4] -= kwiat[4]
                                hero[4] -= 1
                                break
                            print(f"\tKwiat hp {kwiat[0]} atak {kwiat[1]} ")
                            print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                            print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                            inp = input("co robisz: ").lower()
                            if inp == "a":
                                if hero[4] >= 1:
                                    kwiat[0] -= hero[1]
                                    hero[4] -= 1
                                elif hero[4] == 0:
                                    kwiat[0] -= hero[1]
                                    hero[0] -= kwiat[1]
                            elif inp == "e":
                                print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                inp = input("co bierzesz: ")
                                if inp == "l":
                                    if Eq[0] == 0:
                                        break
                                    elif Eq[0] >= 1:
                                        Eq[0] -= 1
                                        hero[0] += 50
                                        print("smakuje jak zywiec jasne pełne")
                                elif inp == "m":
                                    if Eq[1] == 0:
                                        break
                                    elif Eq[1] >= 1:
                                        Eq[1] -= 1
                                        hero[2] += 50
                                        print("smakuje jak Zubr jasne pełne")
                            elif inp == "o":
                                if hero[4] == 0:
                                    hero[4] += 1
                                elif hero[4] == 1:
                                    hero[4] -= 1
                                    hero[0] -= kwiat[1]
                                    print("za długo trzymałes obrone kwiat znalazł słaby punkt")
                                    time.sleep(2)
                            elif inp == "z":
                                if Eq[3] == 0:
                                    print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                    hero[0] -= kwiat[1]
                                elif Eq[2] < 25:
                                    print("nie masz wystarczajaco many")
                                elif Eq[3] <= 1:
                                    print("FIER_BALL!!!")
                                    time.sleep(2)
                                    kwiat[0] -= 125
                                    hero[2] -= 25
                            else:
                                print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                hero[0] -= kwiat[1]
                            time.sleep(1)
                            os.system('cls')
                    elif inp == "b":
                        while True:
                            if hero[0] < 0:
                                print("UMARLES")
                                break
                            elif zioła[4] == 0:
                                print("Nie ma wiecej Ziół")
                                time.sleep(2)
                                break
                            elif zioła[0] < 0:
                                print(f"WOW! Zloto! {zioła[3]}")
                                hero[3] += zioła[3]
                                print(f"WOW! Zioła! {zioła[4]}")
                                materiały[2] += zioła[4]
                                zioła[4] -= zioła[4]
                                hero[4] -= 1
                                break
                            print(f"\tZioła hp {zioła[0]} atak {zioła[1]} ")
                            print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                            print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                            inp = input("co robisz: ").lower()
                            if inp == "a":
                                if hero[4] >= 1:
                                    zioła[0] -= hero[1]
                                    hero[4] -= 1
                                elif hero[4] == 0:
                                    zioła[0] -= hero[1]
                                    hero[0] -= zioła[1]
                            elif inp == "e":
                                print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                inp = input("co bierzesz: ")
                                if inp == "l":
                                    if Eq[0] == 0:
                                        break
                                    elif Eq[0] >= 1:
                                        Eq[0] -= 1
                                        hero[0] += 50
                                        print("smakuje jak zywiec jasne pełne")
                                elif inp == "m":
                                    if Eq[1] == 0:
                                        break
                                    elif Eq[1] >= 1:
                                        Eq[1] -= 1
                                        hero[2] += 50
                                        print("smakuje jak Zubr jasne pełne")
                            elif inp == "o":
                                if hero[4] == 0:
                                    hero[4] += 1
                                elif hero[4] == 1:
                                    hero[4] -= 1
                                    hero[0] -= zioła[1]
                                    print("za długo trzymałes obrone zioła znalazł słaby punkt")
                                    time.sleep(2)
                            elif inp == "z":
                                if Eq[3] == 0:
                                    print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                    hero[0] -= zioła[1]
                                elif Eq[2] < 25:
                                    print("nie masz wystarczajaco many")
                                elif Eq[3] <= 1:
                                    print("FIER_BALL!!!")
                                    time.sleep(2)
                                    zioła[0] -= 125
                                    hero[2] -= 25
                            else:
                                print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                hero[0] -= zioła[1]
                            time.sleep(1)
                            os.system('cls')
                    elif inp == "c":
                        while True:
                            if hero[0] < 0:
                                print("UMARLES")
                                break
                            elif grzyby[4] == 0:
                                print("Nie ma wiecej Grzybów")
                                time.sleep(2)
                                break
                            elif grzyby[0] < 0:
                                print(f"WOW! Zloto! {grzyby[3]}")
                                hero[3] += grzyby[3]
                                print(f"WOW! Grzyby! {grzyby[4]}")
                                materiały[4] += grzyby[4]
                                grzyby[4] -= grzyby[4]
                                hero[4] -= 1
                                break
                            print(f"\tGrzyby hp {grzyby[0]} atak {grzyby[1]} ")
                            print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                            print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                            inp = input("co robisz: ").lower()
                            if inp == "a":
                                if hero[4] >= 1:
                                    grzyby[0] -= hero[1]
                                    hero[4] -= 1
                                elif hero[4] == 0:
                                    grzyby[0] -= hero[1]
                                    hero[0] -= grzyby[1]
                            elif inp == "e":
                                print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                                inp = input("co bierzesz: ")
                                if inp == "l":
                                    if Eq[0] == 0:
                                        break
                                    elif Eq[0] >= 1:
                                        Eq[0] -= 1
                                        hero[0] += 50
                                        print("smakuje jak zywiec jasne pełne")
                                elif inp == "m":
                                    if Eq[1] == 0:
                                        break
                                    elif Eq[1] >= 1:
                                        Eq[1] -= 1
                                        hero[2] += 50
                                        print("smakuje jak Zubr jasne pełne")
                            elif inp == "o":
                                if hero[4] == 0:
                                    hero[4] += 1
                                elif hero[4] == 1:
                                    hero[4] -= 1
                                    hero[0] -= grzyby[1]
                                    print("za długo trzymałes obrone grzyby znalazł słaby punkt")
                                    time.sleep(2)
                            elif inp == "z":
                                if Eq[3] == 0:
                                    print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                    hero[0] -= grzyby[1]
                                elif Eq[2] < 25:
                                    print("nie masz wystarczajaco many")
                                elif Eq[3] <= 1:
                                    print("FIER_BALL!!!")
                                    time.sleep(2)
                                    grzyby[0] -= 125
                                    hero[2] -= 25
                            else:
                                print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                                hero[0] -= grzyby[1]
                            time.sleep(1)
                            os.system('cls')                                                      
            elif inp == "g":
                print("\tSPOTKAŁES GOBLINA !!!")
                print("\t\tWALKA !!!")
                    # if czas[0] > 3:
                    #     print("jest za puzno")
                    #     break
                while True:
                        if hero[0] < 0:
                            print("UMARLES")
                            break
                        elif goblin[4] == 0:
                            print("Nie ma wiecej goblinów")
                            time.sleep(2)
                            break
                        elif goblin[0] < 0:
                            print(f"WOW! Zloto! {goblin[3]}")
                            hero[3] += goblin[3]
                            print(f"WOW! Goblin-core! {goblin[4]}")
                            materiały[5] += goblin[4]
                            goblin[4] -= goblin[4]
                            print(f"WOW! pazury {goblin[5]} \nWOW! uszy {goblin[6]}")
                            materiały[8] += goblin[5]
                            materiały[9] += goblin[6]
                            hero[4] -= 1
                            break
                        print(f"\tgoblin hp {goblin[0]} atak {goblin[1]} ")
                        print(f"\tHero: hp: {hero[0]} atak: {hero[1]} obrona: {hero[4]}")
                        print("\ta - atak \to - obrona \tz - zaklecia \te - ekwipunek")
                        inp = input("co robisz: ").lower()
                        if inp == "a":
                            if hero[4] >= 1:
                                goblin[0] -= hero[1]
                                hero[4] -= 1
                            elif hero[4] == 0:
                                goblin[0] -= hero[1]
                                hero[0] -= goblin[1]
                        elif inp == "e":
                            print("\tjaką potke wybierasz \n \tl - potke leczenia \n \tm -potke many")
                            inp = input("co bierzesz: ")
                            if inp == "l":
                                if Eq[0] == 0:
                                    break
                                elif Eq[0] >= 1:
                                    Eq[0] -= 1
                                    hero[0] += 50
                                    print("smakuje jak zywiec jasne pełne")
                            elif inp == "m":
                                if Eq[1] == 0:
                                    break
                                elif Eq[1] >= 1:
                                    Eq[1] -= 1
                                    hero[2] += 50
                                    print("smakuje jak Zubr jasne pełne")
                        elif inp == "o":
                            if hero[4] == 0:
                                hero[4] += 1
                            elif hero[4] == 1:
                                hero[4] -= 1
                                hero[0] -= goblin[1]
                                print("za długo trzymałes obrone goblin znalazł słaby punkt")
                                time.sleep(2)
                        elif inp == "z":
                            if Eq[3] == 0:
                                print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                                hero[0] -= goblin[1]
                            elif Eq[2] < 25:
                                print("nie masz wystarczajaco many")
                            elif Eq[3] <= 1:
                                print("FIER_BALL!!!")
                                time.sleep(2)
                                goblin[0] -= 125
                                hero[2] -= 25
                        else:
                            print("Ehhh stoisz w szoku i nic nie robisz... Ahhh...")
                            hero[0] -= goblin[1]
                        time.sleep(1)
                        os.system('cls')  
    elif inp == "z":
        while True:
            print(f"\tMATERIAŁY: ({materiały[0]}) ruda-metalu: ({materiały[1]}) sztabka-metalu: ({materiały[2]}) zioła: ({materiały[3]}) kwiaty:")
            print(f"\t\t   ({materiały[4]}) grzyby: ({materiały[5]}) goblin-core: ({materiały[6]}) slime-core: ({materiały[7]}) boss-core:")
            print(f"\t\t   ({materiały[8]}) pazury-goblina: ({materiały[9]}) uszy-goblina: ({materiały[10]}) esencja-slima:")
            print(f"\tEKWIPUNEK: ({Eq[0]}) potka-leczenia: ({Eq[1]}) potka-many ({Eq[2]*1/5}) kolofy ({Eq[3]}) zaklecia")
            print("==="*27)
            print("klikni ~Z~ zeby przestac ogladac ekwipunek")
            print("==="*27)
            inp = input("-- ")
            if inp == "z":
                break 
    elif inp == "b":
        print("Wszedłes do miasta gdzie idzesz ?")
        while True:
            print("""\tk - idzesz do kowala \n \td - idzesz do shamana \n \tt - targu \n \ts - spierdalam stad""")
            print(""" """)
            inp = input("\t--gdzie idzesz--").lower()
            if inp == "d":
                print("""\tp - potka-leczenia \n \tm - potka-many \n \tk - kup-zaklecia \n \ts - spzedarz_boss-cora """)
                inp = input("\t--co robisz--").lower()
                if inp == "p":
                    if hero[3] < 15:
                        print("nie stac cie")
                        break
                    elif materiały[2] < 30:
                        print("nie mam ziół")
                        break
                    elif materiały[3] < 15:
                        print("nie mam kwiatków")
                        break
                    elif materiały[4] < 10:
                        print("nie mam grzybów")
                        break
                    elif materiały[5] < 3:
                        print("nie mam goblin-corów")
                        break
                    elif materiały[5] >= 3:
                        print("Wiedzma upichciła ci potki na hp masz ich 3 ")
                        hero[3] -= 15
                        materiały[2] -= 30
                        materiały[3] -= 15
                        materiały[4] -= 10
                        materiały[5] -= 3
                        Eq[0] += 3
                elif inp == "m":
                    if hero[3] < 30:
                        print("nie stac cie")
                        break
                    elif materiały[2] < 45:
                        print("nie mam ziół")
                        break
                    elif materiały[3] < 28:
                        print("nie mam kwiatków")
                        break
                    elif materiały[6] < 6:
                        print("nie mam goblin-corów")
                        break
                    elif materiały[6] >= 6:
                        print("Wiedzma upichciła ci potki na Mp masz ich 3 ")
                        hero[3] -= 30
                        materiały[2] -= 45
                        materiały[3] -= 28
                        materiały[5] -= 6
                        Eq[1] += 3
                elif inp == "k":
                    if hero[3] < 45:
                        print("nie stac mnie")
                        break
                    elif hero[3] < 85:
                        print("dostałes ksiege zakec nauczyłes sie fier-ball")
                        Eq[3] += 1
                        hero -= 85
            elif inp == "k":
                print("""\tm - miecz \n \tz - zbroja \n \tp - przetop-metalu """)
                inp = input("\t--co robisz--").lower()
                if inp == "p":
                    if materiały[0] == 0:
                        print("Nie mam materiałów")
                        time.sleep(1)
                    elif hero[3] < 5:
                        print("nie masz piataka za przeróbke")
                    elif materiały[0] > 0:
                        print("Przetapiasz minerały na sztapki metalu")
                        materiały[0] -= materiały[0]
                        materiały[1] += materiały[0]
                        hero[3] -= 5
                elif inp == "z":
                    if hero[3] < 89:
                        print("\tnie stac mnie")
                        break
                    elif materiały[1] < 30:
                        print("\tnie mam materiałów")
                    elif materiały[1] > 30:
                        hero[4] += 5
                        hero[3] -= 89
                        materiały[1] -= 30
                elif inp == "m":
                    if hero[3] < 49:
                        print("\tnie stac mnie")
                        break
                    elif materiały[1] < 15:
                        print("\tnie mam materiałów")
                    elif materiały[1] > 15:
                        hero[1] += 5
                        hero[3] -= 49
                        materiały[1] -= 15
            # elif inp == "g":
            #     randint(0,6)
            #     if randint == 0:
            #         print("\tdostałes quest zbierania ziół")
            #         inp = input("\ta akceptujesz \to odrzucasz")
            #         if inp == "a":
            #             if print("o"):
            #                 break
            elif inp == "t":
                print("""\tj - jabuszko \n \ta - arbuz \n \tk - kilof """)
                inp = input("\t--co kupujesz--").lower()
                if inp == "j":
                    print("\t ~~mmm~~ smaczne jabuszko ~~mmm~~")
                    hero[0] += 1
                    hero[3] -= 3
                    time.sleep(2)
                elif inp == "a":
                    print("\t a gdzie fried chicken??!!??!!")
                    hero[0] += 1
                    hero[3] -= 4
                    time.sleep(2)
                elif inp == "k":
                    if hero[3] < 25:
                        print("nie stac cie")
                        break
                    elif hero[3] >= 25:
                        print("zdobyłes kilof miłego kopania")
                        hero[3] -= 25
                        Eq[2] += 5
            elif inp == "s":
                break
            time.sleep(1)
            os.system('cls')
        pass
    elif inp == "c":
        print("przyleciał smok i cie zabił")
        break
    else:
        print("Siedzi bezczynie w swiecie Isekai! Cogratulations!")
    time.sleep(1)
    os.system('cls')