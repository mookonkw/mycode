# OOP

#Zork protagonist

class Adventurer():
    #class attribute
    # what is in their pockets?
    #what is their health?
    #how hard can they swing a sword?

    def __init__(self):
        #attributes
        self.inventory = ["candle" , "book of matches"]
        self.health= 10
        self.strength= 5

    def potion(self) :
        # drink a healing potion
        self.health +=5
    
    def punch(self, other_adventurer: Adventurer()):
        other_adventurer.health -= self.strength
        #apply ones strength against anothers health


nahIla = Adventurer()
Asberus = Adventurer()

# print(nahIla.health)
print(Asberus.health)

nahIla.punch(Asberus)

print(Asberus.health)

# input("Asberus chugs a health potion!")
# Asberus.potion()

# print(nahIla.health)
# print(Asberus.health)



