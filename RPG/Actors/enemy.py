#Classe inimigo
import random
import Sistems.damage as Damage
import character as Character

class Enemy(Damage,Character):
    def __init__(self,nome,hp,defense,strg,dex):
        self.nome = nome # Nome do inimigo
        self.hp = hp # Pontos de vida
        self.defense = defense # Defesa
        self.strg = strg # Força (Dano em si)
        self.dex = dex # Deztreza (Usado para calcular a evasão,precisão e velocidade do ataque)
        
class Skeleton(Enemy):
    def __init__(self):
        super().__init__(nome="Esqueleto",hp=120,defense=200,strg=10,dex=25)