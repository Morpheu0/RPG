#Classe de personagens

import Sistems.classes as Classes
import os,json

char = {}
data_dir = 'DB'
data_name = 'char.json'
file_path = os.path.join(data_dir, data_name)

class Character(Classes):
    def __init__(self,nome,idade,tamanho,peso,raca,genero,nivel,xp):
        self.nome = nome
        self.idade = idade
        self.tamanho = tamanho
        self.peso = peso
        self.raca = raca
        self.genero = genero
        self.nivel = nivel
        self.xp = xp
                
    def char_making(self):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        self.nome = input("Nome do personagem: \n")
        self.idade = int(input("Idade: \n"))
        self.tamanho = float(input("Tamanho do char: \n"))
        self.peso = float(input("Peso do char: \n"))
        self.raca = input("Raça do char: \n")
        while True:
            self.genero = int(input("Gênero do char: [1]M [2]F"))
            if  1 == self.genero == 2 :
                break
            else:
                print("Escolha inválida!")
        self.nivel = 0
        self.xp = 0.0
        char[self.nome] = [
                self.idade,
                self.tamanho,
                self.peso,
                self.raca,
                self.genero,
                self.nivel,
                self.xp
            ]
        with open(file_path,'w') as json_file:
            json.dump(char,json_file,indent=4)
        
    def level_up(self):
        self.qntdxp = 100
        if self.xp >= self.qntdxp:
            self.nivel += 1
            self.xp = 0
            self.qntdxp *= 1.5
        
        
    