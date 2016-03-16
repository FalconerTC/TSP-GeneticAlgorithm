import random
from Tour import Tour
from random import randint

class Genalgo(object):

    def __init__(self, lx, ly,
                limit=100, size=50,
                prob_crossover=0.9, prob_mutation=0.2):
        self.lx = lx
        self.ly = ly
        self.limit = limit
        self.size = size
        self.prob_crossover = prob_crossover
        self.prob_mutation = prob_mutation
        self.tours = [Tour(self.lx, self.ly) for i in range(0, size)]

    def initialize(self):
        t = Tour(self.lx, self.ly)
        print t.get_cost(), t.get_fitness()
        print self.get_fittest().get_cost()

    def evolve_new_pop(self):
        pass

    def evolve_same_pop(self):
        pass

    def crossover(self,parent1,parent2):
        child1 = [-1 for x in range(len(parent1))]
        child2 = [-1 for x in range(len(parent2))]

        #Used to find ones that weren't duplicates later on
        difflist = []
        difflist2 = []

        count = 0
        count2 = 0

        if len(parent1) != len(parent2):
                print "Trying to crossover two parents that aren't the same length"

        index1 = randint(0,len(parent1))
        index2 = randint(0,len(parent2))

        if index2 > index1:
            for i in range(index1,index2):
                child1[i] = parent2[i]
                child2[i] = parent1[i]
        elif index2 < index1:
            for i in range(index2,index1):
                child1[i] = parent2[i]
                child2[i] = parent1[i]
        else:
            child1[index1] = parent2[index1]
            child2[index1] = parent1[index1]

        # Finding all the numbers that weren't duplicates from the initial exchange
        for i in range(0,len(parent1)):
            if parent1[i] not in child1:
                difflist.append(parent1[i])
            if parent2[i] not in child2:
                difflist2.append(parent2[i])

        # Adding the non duplicates to the new child in the same order
        for i in range(0,len(parent1)):
            if child1[i] == -1:
                child1[i] = difflist[count]
                count += 1
            if child2[i] == -1:
                child2[i] = difflist2[count2]
                count2 += 1               
        '''
        print index1," ",index2
        print parent1
        print child1
        print parent2
        print child2
        '''
        return child1,child2

    def tournament_selection(self):
        pass

    def mutate(self):
        pass

    def get_fittest(self):
        fittest = self.tours[0]
        for i in self.tours:
            if i.get_fitness() > fittest.get_fitness():
                fittest = i
        return fittest
