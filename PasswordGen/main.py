from pickle import TRUE
from random import choice as c
while TRUE:
    if input() == "generate":
        words = ["Red", "Blue", "Green", "Alpha", "Beta", "Delta", "Dog", "Cat", "Bird"]
        numbers = ["0","1","2","3","4","5","6","7","8","9"]
        print(c(words) + c(words) + c(words) + c(numbers) + c(numbers))