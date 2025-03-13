# WAP a program to fill a letter template givem below with name and date
letter = '''
         Dear <|Name|>
         You are selected!
         <|Date|>
        '''

print(letter.replace("<|Name|>","Monty"))
print(letter.replace("<|Date|>","5-Dec-2005"))