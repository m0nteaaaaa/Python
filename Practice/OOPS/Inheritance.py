class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('Log In')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, no_of_arrows, email):
        super().__init__(email)
        self.name = name
        self.no_of_arrows = no_of_arrows

    def attack(self):
        print(f'Attacking with Arrows : arrows left = {self.no_of_arrows}')
       
class Oger(User):
    def __init__(self,name, strength, email):
        User.__init__(self, email)
        self.name = name
        self.strength = strength

    def attack(self):
        print(f'Attacking with Strength of {self.strength}')

class Cyborg(Wizard, Archer):
    def __init__(self, name, power, arrows , email):
        Archer.__init__(self, name , arrows, email)
        Wizard.__init__(self, name , power, email)

wizard1 = Wizard('Merlin', 50, 'merlin@email.com ')
archer1 = Archer('Robin', 100, 'archer@email.com')
oger1 = Oger('Shrek', 1000, 'oger@email.com')
cyborg1 = Cyborg('Iornman' , 'Full Power',1000 ,'cyborg@email.com')

User.sign_in('monty')

#print(dir(wizard1))