# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:38:14 2021

@author: coach
"""

from random import randint
succFail = []

randString = []

while True:
    letter = input("What are the success or failuer indicators? Enter Q to quit. ")
    if letter == "Q":
        break
    succFail.append(letter)
    
howMany = int(input("How many runs do you need? "))
    
for rndItr in range(0, howMany):
    ranGen = randint(0, 1)
    randString.append(succFail[ranGen])
    
#print(randString)

for attmpt in randString:
    print(attmpt, end="")
    
    
    