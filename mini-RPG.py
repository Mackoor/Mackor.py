from random import randint
import os
import time
# hp atak mana gold
hero = [200,20,100,100]
while hero[0] > 0:
    goblin = [randint(10,100),randint(10,20),randint(0,0),randint(10,250)]
    print("""\ta - idz do lasu \n \tb - idz do miasta""")
    print(f"\thero: hp: {hero[0]} atak: {hero[1]} mana: {hero[2]} gold: {hero[3]}")
    print("==="*10)
    inp = input("co robisz: ").lower()
    if inp == "a":
        print("\t\tWALAKA !!!")
        while True:
            if hero[0] < 0:
                print("UMARLES")
                break
            if goblin[0] < 0:
                print(f"WOW! Zloto! {goblin[3]}")
                hero[3] += goblin[3]
                break
            print(f"\tMonster hp {goblin[0]} atak {goblin[1]}")
            print(f"\tHero: hp: {hero[0]} atak: {hero[1]}")
            print("\ta - atak \tz - zaklecia")
            inp = input("co robisz: ").lower()
            if inp == "a":
                hero[0] -= goblin[1]
                goblin[0] -= hero[1]
            elif inp == "z":
                print("Ohh zapmoniales ze nie znasz jeszcze zaklęć!")
                hero[0] -= goblin[1]
            else:
                print("Ehhh stisz w szoku i nic nie robisz... Ahhh...")
                hero[0] -= goblin[1]
            time.sleep(1)
            os.system('cls')            
    elif inp == "b":
        print("Lokacja misto jeszcze nie istnieje! hehheh...")
        pass
    else:
        print("Siedzi bezczynie w swiecie Isekai! Cogratulations!")
    time.sleep(3)
    os.system('cls')