class Playercharacter:
    def __init__(self,name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def run(self):
        print(f'{self.name} is running')
    
    def shout(self):
        print(f'My name is {self.name} and I am {self.age} years old .//{self.gender}//')

player1 = Playercharacter('Monty', 24, 'Male')
player2 = Playercharacter('Neha', 22, 'Female')

print(player2.shout())
print(player2.run())