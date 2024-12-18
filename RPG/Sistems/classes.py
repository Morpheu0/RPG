#Classe de classes de personagem

import Sistems.damage as Damage
import Actors.character as Character

import json

with open('char.json','r') as json_file:
    data = json.load(json_file)


class Classes(Damage,Character):
    def __init__(self,hp=100,dext=20,strg=30,mana=0):
        self.hp = hp
        self.dex = dext
        self.strg = strg
        self.mana = mana
        self.health()
        
    def health(self):
        self.hp = self.hp * (data[self.nome][self.nivel]  * 0.3)

class Warrior(Classes):
    
    
        