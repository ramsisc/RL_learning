class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("basrkrkrrkkr")
            
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age +=1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

        
ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

ozzy.buddy.doginfo()



# numpy

import numpy as np

