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

    def initialize(self):
        t = Tour(self.lx, self.ly)
        print t.get_cost(), t.get_fitness()

    def evolve(self):
        pass

    def gen_population(self):
        pass
