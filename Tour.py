import random
import math

class Tour(object):

    def __init__(self, lx, ly):
        self.lx = lx
        self.ly = ly
        self.distance = 0
        self.fitness = 0
        self.cities = random.sample(range(len(lx)), len(lx))
        print "Cities: ",self.cities

    def set_tour(self, l):
        self.cities = l
        self.distance = 0
        self.fitness = 0
    
    def get_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / self.get_cost()
        return self.fitness

    # Calculate total distance of tour
    def get_cost(self):
        if self.distance == 0:
            for i in range(1, len(self.cities) + 1):
                p1 = self.cities[i-1]
                p2 = self.cities[i % len(self.cities)]
                self.distance += self.distance_to(p1, p2)
        return self.distance

    # Distance formula between two points
    def distance_to(self, p1, p2):
        xd = self.lx[p1] - self.lx[p2]
        yd = self.ly[p1] - self.ly[p2]
        return math.sqrt(xd*xd + yd*yd)


    pass
