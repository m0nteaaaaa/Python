# WAP to create a dictionary of hindi words with values as their English Trnalsation . Provide user with an option to look it up.

words = {
    "billi" : "cat",
    "kutta" : "dog"
}

word = input("Enter the word you want to know the meaning : ")
print(words.get(word))