from . import enemi as e

gracz = {
        "Hp":100,
        "Dmg":15,
        "Stamina":100,
        "Gold":0,
        "EQ":["Hp_Potion"],
        "Max_Hp":100,
        "Max_Stamina":100
        }


def HP_ITD(gracz,enemy):
    print(f"\t {"="*40} ")
    print(f" \t Twoje Hp - {gracz["Hp"]} Twój Dmg - {gracz["Dmg"]} Twoja Stamina - {gracz["Stamina"]}")       
    print(f" \t Przeciwnika Hp - {enemy["Hp"]} Przeciwnika Dmg - {enemy["Dmg"]}")    
    print(f"\t {"="*40} ")

def gracza(gracz):
    print(f"\t {"="*40} ")
    print(f"\t HP - {gracz["Hp"]} \n \t Stamina - {gracz["Stamina"]} \n \t Dmg - {gracz["Dmg"]}")
    print(f"\t {"="*40} ")

def EQ(gracz):
    print(f"\t {"="*40} ")
    print(f"\t Gold - {gracz['Gold']} \n \t EQ - {gracz["EQ"]}")
    print(f"\t {"="*40} ")

