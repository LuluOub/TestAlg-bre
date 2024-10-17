import random
import string


def choisir():
    fonction = random.choice(string.ascii_lowercase)
    lettre1 = random.choice(string.ascii_uppercase)
    lettre2 = random.choice(string.ascii_uppercase)
    lettre3 = random.choice(string.ascii_uppercase)
    lettre4 = random.choice(string.ascii_uppercase)
    print(lettre1,",",lettre2,",",lettre3,",",lettre4,"désignent quatre ensembles non vides tels que",lettre3,"inclus",lettre1,"et",lettre4,"inclus",lettre1,'.')
    print("Soit",fonction,":",lettre1,"-->",lettre2,"une fonction")
