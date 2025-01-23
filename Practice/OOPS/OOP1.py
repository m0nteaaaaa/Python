  #OOP

class PlayerCharacter:
    #Class Object Attribute b        
    membership = True
    def __init__(self, name="anonymous",age=0):
        if(age>18):
            self.name = name #attributes
            self.age = age

    def run(self): 
        print('run') #methods
        return 'done'
    
    def shout(self):
        print(f'my name is {self.name} and my age is {self.age}')

player1 = PlayerCharacter('Cindy',22)
player2 = PlayerCharacter('Tom',21)
player2.attack = 50

print(player1.shout())
print(player2.shout())

print(player1.name)
print(player1.run())

print(player2.age)
print(player2.attack)

print(player1.membership)