#OOP
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name #attribute
        self.age = age
    
    def shout(self):
        print(f'my name is {self.name}')
        return 'done'

    @classmethod
    def adding_things(cls,num1, num2):
        return cls('Teddy',num1 + num2)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2

player3 = PlayerCharacter.adding_things(2,3)
print(player3.name)
