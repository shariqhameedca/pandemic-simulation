import random
import numpy as np

class Person:
    def __init__(self, startingImmunity):
        if random.randint(0,100) < startingImmunity:
            self.immunity = True
        else:
            self.immunity = False
        
        self.contagiousness = 0
        self.mask = 0
        self.contagiousDays = 0
        self.friends = int((np.random.normal(size=1,loc=0.5,scale=0.15)[0]*10).round(0))
        self.obeylockdown = False
        
    def wearMask(self):
        self.contagiousness /= 2