import random
from Tour import Tour
from random import randint

class Genalgo(object):

    def __init__(self, lx, ly,
                limit=100, size=100,
                prob_crossover=0.9, prob_mutation=0.1, tournament_size=5):
        self.lx = lx
        self.ly = ly
        self.limit = limit
        self.size = size
        self.tournament_size = tournament_size
        self.prob_crossover = prob_crossover
        self.prob_mutation = prob_mutation
        self.tours = [Tour(self.lx, self.ly) for i in range(0, size)]

    def initialize(self):
        t = Tour(self.lx, self.ly)

    def evolve_new_pop(self):
        new_tours = []

        # Save best tour
        _, best_tuple = self.get_best_tours(self.tours)
        best = self.tours[best_tuple[0]]
        new_tours.append(best)

        for i in range(1, len(self.tours)):
            parent1 = self.tournament_selection()
            parent2 = self.tournament_selection()
            print parent1, parent2
            child1, child2 = self.crossover(parent1, parent2)
        pass

    def evolve_same_pop(self):
        bestTwo = self.get_best_tours(self.tours)
        worstTwo = self.get_worst_tours(self.tours)

        child1List,child2List = self.crossover(self.tours[bestTwo[0][0]].cities,
                self.tours[bestTwo[1][0]].cities)

        #print "Best: ", self.tours[bestTwo[1][0]].cities ,bestTwo[1][1]
        print "Best: ", bestTwo[1][1]
        
        #print "Cost: ", self.tours[bestTwo[1][0]].get_cost()

        child1 = Tour(self.lx, self.ly)
        child2 = Tour(self.lx, self.ly)

        child1.set_tour(child1List)
        child2.set_tour(child2List)

       # print "New Children scores: ",child1.get_cost(), " and: ",child2.get_cost()

        if self.tours[worstTwo[0][0]].get_cost() > child1.get_cost():
            self.tours[worstTwo[0][0]] = child1

        if self.tours[worstTwo[1][0]].get_cost() > child2.get_cost():
            self.tours[worstTwo[1][0]] = child2

        for i in range(len(self.tours)):
            self.tours[i] = self.mutate(self.tours[i])

        pass

    def crossover(self, parent1, parent2):
        child1 = [-1 for x in range(len(parent1))]
        child2 = [-1 for x in range(len(parent2))]

        #Used to find ones that weren't duplicates later on
        difflist = []
        difflist2 = []

        count = 0
        count2 = 0

        if len(parent1) != len(parent2):
                print "Trying to crossover two parents that aren't the same length"

        # Generate random bounds
        index1 = randint(0, len(parent1)-1)
        index2 = randint(0, len(parent2)-1)

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

        #print index1," Through ",index2, " for the crossover"
        '''
        print parent1
        print child1
        print parent2
        print child2
        '''
        return child1,child2

    def get_best_tours(self, tour_list):
        bestTwo = [(-1,10000),(-1,10000)]
        for i in range(len(tour_list)):
            currentCost = tour_list[i].get_cost()
            if currentCost < bestTwo[0][1] and currentCost < bestTwo[1][1]:
                bestTwo[0] = (bestTwo[1])
                bestTwo[1] = (i, currentCost)
            elif currentCost < bestTwo[0][1]:
                bestTwo[0] = (i, currentCost)
        return bestTwo

    def get_worst_tours(self, tour_list):
        worstTwo = [(-1,0),(-1,0)]
        for i in range(len(tour_list)):
            currentCost = tour_list[i].get_cost()
            if currentCost > worstTwo[0][1] and currentCost > worstTwo[1][1]:
                worstTwo[0] = (worstTwo[1])
                worstTwo[1] = (i, currentCost)
            elif currentCost > worstTwo[0][1]:
                worstTwo[0] = (i, currentCost)
        return worstTwo

    def tournament_selection(self):
        rand_tours = [randint(0, len(self.tours)) for x in range(self.tournament_size)]
        second, best_tuple = self.get_best_tours(rand_tours)
        return self.tours[best_tuple[0]]

    def mutate(self,tour):
        index1 = randint(0, len(tour.cities)-1)
        index2 = randint(0, len(tour.cities)-1)
        if random.random()<self.prob_mutation:
           # print "Mutating: ",tour.cities[index1], " ", tour.cities[index2]
            tour.swap(index1,index2)
        return tour

    def get_fittest(self):
        fittest = self.tours[0]
        for i in self.tours:
            if i.get_fitness() > fittest.get_fitness():
                fittest = i
        return fittest
