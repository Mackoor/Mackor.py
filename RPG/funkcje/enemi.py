from random import randint
        
enemy = [
        {
            "type":"goblin",
            "Hp": randint(50,75),
            "Dmg": randint(5,15),
            "Gold": randint(2,13),
            "Loot":["ucho_goblina","ucho_goblina","kieł_goblina"],
            "Max_hp": randint(50,75)
        },
        {
            "type":"wilk",
            "Hp": randint(40,60),
            "Dmg": randint(5,15),
            "Gold": 0,
            "Loot":["ucho_wilka","kieł_wilka","kieł_wilka","futro_wilka"],
            "Max_hp": randint(40,60)
        },
        {
            "type":"szkielet",
            "Hp": randint(80,100),
            "Dmg": randint(15,25),
            "Gold": randint(10,25),
            "Loot":["Kosc","łuk"],
            "Max_hp": randint(80,100)
        },
        {
            "type":"Nieumarły",
            "Hp": randint(100,120),
            "Dmg": randint(20,30),
            "Gold": randint(20,35),
            "Loot":["serce_nieumarłego","palec","miecz"],
            "Max_hp": randint(100,120)
        }
        ]
def reset_enemy(enemy):

    enemy["Hp"] = enemy["Max_hp"]