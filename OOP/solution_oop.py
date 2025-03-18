class character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def attack_enemy(self):
        print(f"{self.name} attacsk with power {self.attack}")

warior = character('Thor',100,50)
hasnain = character('Gandalf' , 80, 70)

warior.attack_enemy()
hasnain.attack_enemy()