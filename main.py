import random
import time
import numpy as np
from Person import Person
from matplotlib import pyplot as plt

populationList = []

# This Function begins the simulation by asking for some necessary factors of the simulation such as
# 1. Starting Population - Total population 
# 2. Starting Immunity - Number of people already immune to the disease
# 3. Starting infectors - Number of people infected at day 0
# 4. DaysContagious - Number of days a person stays contagious
# 5. locdownDay - The day at which lockdown is announced
# 6. lockdownPercentage - Percentage of people who obey lockdown
# 7. maskDay - The day at which mask is announced mandatory
# 8. maskPercentage - Percentage of people who wear face mask

def beginSim():
    startingPopulation = int(input("Starting Population"))
    startingImmunity = int(input("Percentage of people with natural immunity"))
    startingInfecters = int(input("How many people will be infectious at the beginning"))
    
    for x in range(startingPopulation):
        populationList.append(Person(startingImmunity))
        
    for x in range(0, startingInfecters):
        populationList[random.randint(0,len(populationList)-1)].contagiousness = int((np.random.normal(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
        
    daysContagious = int(input("Days Contagious"))
    lockdownDay = int(input("At which day lockdown will be declared"))
    lockdownPercentage = int(input("How much percentage of people will obey lockdown"))
    maskDay = int(input("At which day mask will be announced mandatory"))
    maskPercentage = int(input("How much percentage of people will obey facemask"))
    return daysContagious, lockdownDay,lockdownPercentage, maskDay, maskPercentage

# This function runs a day and calculate the total infected, total immuned people
def runDay(daysContagious, lockdown):
    for person in [person for person in populationList if person.contagiousness > 0  and person.friends > 0]:
        couldMeetFriends = int(person.friends/2)
        if couldMeetFriends > 0:
            metFriends = random.randint(0, couldMeetFriends)
        else:
            metFriends = 0
            
        if person.obeylockdown == True:
            metFriends = 0
            
        for x in range(metFriends):
            friend = populationList[random.randint(0,len(populationList)-1)]
            if random.randint(0,100) < person.contagiousness and friend.contagiousness == 0 and friend.immunity == False:
                friend.contagiousness = int((np.random.normal(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
                print(populationList.index(person), " >>> ", populationList.index(friend))
                
    for person in [person for person in populationList if person.contagiousness > 0]:
        person.contagiousDays += 1
        if person.contagiousDays >= daysContagious:
            person.contagiousness = 0
            person.immunity = True
            print(populationList.index(person), "has become immune")

# This is to run the simulation for 100 days
lockdown = False
daysContagious, lockdownDay,lockdownPercentage, maskDay, maskPercentage = beginSim()
infectedTrack = []
for x in range(0,100):
    if x==lockdownDay:
        for person in populationList[0: int(len(populationList) * (lockdownPercentage/100))]:
            person.obeylockdown = True
        
    if x == maskDay:
        for person in populationList[0: int(len(populationList) * (maskPercentage/100))]:
            person.wearMask()

    runDay(daysContagious,lockdown)
    infectedTrack.append(len([person for person in populationList if person.contagiousness > 0]))

plt.plot(range(0,100), infectedTrack)
plt.xlabel("Days")
plt.ylabel("Number of people infected")
plt.title("Infected people vs Days")
plt.show()