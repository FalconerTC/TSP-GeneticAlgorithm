import random
from Tour import Tour

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

    def crossover(self):
        pass

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

