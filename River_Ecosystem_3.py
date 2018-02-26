import random
from random import shuffle
import types

#--------------#
# Animal Class #
#--------------#
class Animal:

    #Constructor
    def __init__(self,movement=0):
        self.__movement = movement

    #Create a method to determine class name
    def getClassName(self):
        return self.__class__.__name__

    def setMovement(self,val):
        self.__movement = val

    def getMovement(self):
        return self.__movement

#---------------------------------#
# Bear Class inherits from Animal #
#---------------------------------#
class Bear(Animal):

    #Constructor
    def __init__(self):
        Animal.__init__(self)
#---------------------------------#
# Fish Class inherits from Animal #
#---------------------------------#
class Fish(Animal):

    #Constructor
    def __init__(self):
        Animal.__init__(self)
#-------------#
# River Class #
#-------------#
class River:

    """This river is basically a list that holds animals"""

    #Initialise with a random number of fish and bears
    def __init__(self,list_length):

        print "River Object was Created\n"

        self.__length = list_length
        self.__riverContents = [None] * self.__length

        #Fill 50% of list with animals randomly
        for i in range(self.__length/2):

            randomAnimal = random.randint(1,2)

            #Add a Fish to the river if value is a 1
            if randomAnimal == 1:
                self.__riverContents[i] = Fish()

            #Add a Bear to the river if value is 2
            else:
                self.__riverContents[i] = Bear()

        shuffle(self.__riverContents)

    #Get the length of the river
    def getLen(self):
        return self._length

    #Figure out what Animal is in the kth position of the river
    def getItem(self,k):
        return self.__riverContents[k]

    #Set an Animal in the River
    def setItem(self,k,obj):
        self.__riverContents[k] = obj

    #Count the number of free spaces in the river
    def getFreeRiverSpace(self):
        return self.__riverContents.count(None)

    #Add an animal to the river if we have free space
    def addAnimal(self,animal):

        if self.getFreeRiverSpace() > 0: #<--Check if the animal has free space to spawn

            #Create a list of indexes that represent empty positions for animals to spawn
            position = []
            for index, obj in enumerate(self.__riverContents):
                if obj is None:
                    position.append(index)

            spawn_point = random.choice(position) #Get a random index for the spawn point
            self.__riverContents[spawn_point] = animal

    def updateAnimalPosition(self,k):

        #Change animal position only if the animal exists
        if self.__riverContents[k] is not None:

            animal_move = random.randint(-1,1) #Animals can move forward +1, backward -1, or stay still 0

            #Okay the animal can move forward or backward in list
            #unless it is at the beginning or end of the list, then it
            #can only move forward or backward respectively, or stay put.

            #Make animal move if it can, if not stay put.
            if (animal_move != 0) and (0 <= k + animal_move < self.__length):

                #Move into position if no animal is there, dont spawn any young.
                if self.__riverContents[k + animal_move] is None:
                    self.__riverContents[k + animal_move] = self.__riverContents[k]
               
                    print "%s [%d] moved %d" % (self.__riverContents[k].getClassName(),k,animal_move)
                    self.__riverContents[k] = None
    
                #If the animals are the same type, create a baby animal, and hold position of parents.
                elif (self.__riverContents[k].getClassName() == self.__riverContents[k + animal_move].getClassName()):

                    #Add a baby bear cub
                    if self.__riverContents[k].getClassName() == "Bear":
                        self.addAnimal(Bear())
                        print "Bear Created"

                    #Add a tiny tiny fish
                    else:
                        self.addAnimal(Fish())
                        print "Fish Created"


                    self.__riverContents[k].setMovement(animal_move)
                    print "%s [%d] tried to move but found a mate %d" % (self.__riverContents[k].getClassName(),k,animal_move)
                  

                #If this condition is met this means a bear has met a fish,
                #or fish has met a bear.... the fisssssh must DIEEEE!!!!
                else:
                    if self.__riverContents[k].getClassName() == "Bear":
                        self.__riverContents[k + animal_move] = self.__riverContents[k]

                    print "Fish eaten"
                    print "%s [%d] moved %d" % (self.__riverContents[k].getClassName(),k,animal_move)
                    self.__riverContents[k].setMovement(animal_move)
                    self.__riverContents[k] = None

            else:
            	print "%s [%d] did not move %d" % (self.__riverContents[k].getClassName(),k,animal_move)
              


    #Perform movement of all animals for the river
    def updateRiverState(self):
        for i in range(self.__length):
            self.updateAnimalPosition(i)
            self.printRiverState(i)

    #Print out the current state of the river
    def printRiverState(self,k):

        for index, obj in enumerate(self.__riverContents):
            if obj is not None:
                if obj.getClassName() == "Bear":
                    if k == index:
                        print "[%d][ Bear ] <-" % (index)
                    else:
                        print "[%d][ Bear ]" % (index)
                elif obj.getClassName() == "Fish":
                    if k == index:
                        print "[%d][ Fish ] <-" % (index)
                    else:
                        print "[%d][ Fish ]" % (index)	
            else:
                if k == index:
                    print "[%d][      ] <-" % index
                else:
                    print "[%d][      ]" % index

        print "\n"

    #Run the simulation until a certain percentage of the river is full.
    def runSimulation(self,percentage):

        count = 0
        while True:
            if self.getFreeRiverSpace()/float(self.__length) <= (1 - percentage): # > .75 full implies break == <= .25 empty implies break
                break
            else:
                print "#---------Year:%d---------#\n" % (count + 1)
                self.updateRiverState()
                count = count + 1

#Start the river simulation eco-system program
river = River(10)
print "The beginning :)"
river.printRiverState(None)
river.runSimulation(0.75)
