from . import gracz as g
from . import enemi as e
from random import randint

def kopniecie(gracz:dict,enemy):
    if g.gracz["Stamina"] >= 3:
        e.enemy[0]["Hp"] -= g.gracz["Dmg"]*0.4
        g.gracz["Stamina"] -= 3
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]
    elif g.gracz["Stamina"] < 3:
        print(f"\t {"="*40} ")
        print(f"\t Nie masz siły uzyc tego ruchu \n Wróg wykozystuje to tracisz {e.enemy[0]["Dmg"]}Hp")
        print(f"\t {"="*40} ")
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]         

def slach(gracz:dict,enemy):
    if g.gracz["Stamina"] >= 10:
        e.enemy[0]["Hp"] -= g.gracz["Dmg"]
        g.gracz["Stamina"] -= 10
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]
    elif g.gracz["Stamina"] < 10:
        print(f"\t {"="*40} ")
        print(f"\t Nie masz siły uzyc tego ruchu \n Wróg wykozystuje to tracisz {e.enemy[0]["Dmg"]}Hp")
        print(f"\t {"="*40} ")
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]  
 
def heavy_slach(gracz:dict,enemy):
    if g.gracz["Stamina"] >= 18:
        e.enemy[0]["Hp"] -= g.gracz["Dmg"]*1.8
        g.gracz["Stamina"] -= 18
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]
    elif g.gracz["Stamina"] < 18:
        print(f"\t {"="*40} ")
        print(f"\t Nie masz siły uzyc tego ruchu \n Wróg wykozystuje to tracisz {e.enemy[0]["Dmg"]}Hp")
        print(f"\t {"="*40} ")
        g.gracz["Hp"] -= e.enemy[0]["Dmg"]    
        
def odpoczynek(gracz,enemy):
    g.gracz["Stamina"] += 50
    
    if gracz["Stamina"] > gracz["Max_Stamina"]:
        gracz["Stamina"] = gracz["Max_Stamina"]

    print(f"\t {"="*40} ")
    print(f"\t Odpoczołes ale wróg uzył tego momentu tracisz {e.enemy[0]["Dmg"]}Hp")
    gracz["Hp"] -= enemy["Dmg"]
    print(f"\t {"="*40} ")
    

def Potki(gracz):
    if "Hp_Potion" in gracz["EQ"]:
        gracz["EQ"].remove("Hp_Potion")
    
        gracz["Hp"] += 50

        if gracz["Hp"] > gracz["Max_Hp"]:
            gracz["Hp"] = gracz["Max_Hp"]

        print(f"\t {"="*40} ")
        print(f"\t Użyto Potion! +50 Hp \n \t Twoje teraz Hp - {gracz["Hp"]}")
        print(f"\t {"="*40} ")
    else:
        print(f"\t {"="*40} ")
        print("\t Nie masz potionów!")
        print(f"\t {"="*40} ")