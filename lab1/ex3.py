import random


class PairOfDice:
    def __init__(self):
        self.roll()
       

    def roll(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        
    def total(self):
        return self.die1 + self.die2
         
        
        
     
        
    
    
some_dice = PairOfDice()
count = 0
for i in range(0, 1000):
    some_dice.roll()
    if some_dice.total() == 7:
        count+= 1
        
print('# of times you rolled a 7: {}'.format(count))