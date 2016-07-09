"""Genalgo.py."""
import random
from random import randint

from Tour import Tour


class Genalgo(object):
    """Represents a genetic algorithm that can be applied in steps to data."""

    def __init__(self, lx, ly,
                 limit=100, size=10,
                 prob_mutation=0.2, tournament_size=5):
        """Initialize objects."""
        self.lx = lx
        self.ly = ly
        self.limit = limit
        self.size = size
        self.tournament_size = tournament_size
        self.prob_mutation = prob_mutation
        self.tours = [Tour(self.lx, self.ly) for i in range(0, size)]

    def evolve_new_pop(self, iteration):
        """Step algorithm using 'New population' method."""
        new_tours = []

        # Save best tour
        _, best_tuple = self.get_best_tours(self.tours)
        best = self.tours[best_tuple[0]]
        new_tours.append(best)

        for i in range(1, len(self.tours)):
            parent1 = self.tournament_selection()
            parent2 = self.tournament_selection()
            child1, child2 = self.crossover(parent1.cities, parent2.cities)

            t = Tour(self.lx, self.ly)
            t.set_tour(child1)
            new_tours.append(t)

        self.tours = new_tours
        for i in range(1, len(self.tours)):
            self.tours[i] = self.mutate(self.tours[i])

        _, best_tuple = self.get_best_tours(self.tours)
        best = self.tours[best_tuple[0]]

    def evolve_same_pop(self, iteration):
        """Step algorithm using 'Sampe population' method."""
        bestTwo = self.get_best_tours(self.tours)
        worstTwo = self.get_worst_tours(self.tours)

        children1, children2 = self.crossover(self.tours[bestTwo[0][0]].cities,
                                              self.tours[bestTwo[1][0]].cities)

        child1 = Tour(self.lx, self.ly)
        child2 = Tour(self.lx, self.ly)

        child1.set_tour(children1)
        child2.set_tour(children2)

        if self.tours[worstTwo[0][0]].get_cost() > child1.get_cost():
            self.tours[worstTwo[0][0]] = child1

        if self.tours[worstTwo[1][0]].get_cost() > child2.get_cost():
            self.tours[worstTwo[1][0]] = child2

        for i in range(len(self.tours)):
            self.tours[i] = self.mutate(self.tours[i])

    def crossover(self, parent1, parent2):
        """Evolve to get new population."""
        child1 = [-1 for x in range(len(parent1))]
        child2 = [-1 for x in range(len(parent2))]

        # Used to find ones that weren't duplicates later on
        difflist = []
        difflist2 = []
        count = 0
        count2 = 0

        if len(parent1) != len(parent2):
            print("Trying to crossover two parents of different length")

        # Generate random bounds
        index1 = randint(0, len(parent1) - 1)
        index2 = randint(0, len(parent2) - 1)

        if index2 > index1:
            for i in range(index1, index2):
                child1[i] = parent2[i]
                child2[i] = parent1[i]
        elif index2 < index1:
            for i in range(index2, index1):
                child1[i] = parent2[i]
                child2[i] = parent1[i]
        else:
            child1[index1] = parent2[index1]
            child2[index1] = parent1[index1]

        # Find all the numbers that aren't duplicates from the initial exchange
        for i in range(0, len(parent1)):
            if parent1[i] not in child1:
                difflist.append(parent1[i])
            if parent2[i] not in child2:
                difflist2.append(parent2[i])

        # Adding the non duplicates to the new child in the same order
        for i in range(0, len(parent1)):
            if child1[i] == -1:
                child1[i] = difflist[count]
                count += 1
            if child2[i] == -1:
                child2[i] = difflist2[count2]
                count2 += 1

        return child1, child2

    def get_best_tours(self, tour_list):
        """Determine current best tours (shortest distance)."""
        bestTwo = [(-1, 10000), (-1, 10000)]
        for i in range(len(tour_list)):
            currentCost = tour_list[i].get_cost()
            if currentCost < bestTwo[0][1] and currentCost < bestTwo[1][1]:
                bestTwo[0] = (bestTwo[1])
                bestTwo[1] = (i, currentCost)
            elif currentCost < bestTwo[0][1]:
                bestTwo[0] = (i, currentCost)
        return bestTwo

    def get_worst_tours(self, tour_list):
        """Determine current worst tours (longest distance)."""
        worstTwo = [(-1, 0), (-1, 0)]
        for i in range(len(tour_list)):
            currentCost = tour_list[i].get_cost()
            if currentCost > worstTwo[0][1] and currentCost > worstTwo[1][1]:
                worstTwo[0] = (worstTwo[1])
                worstTwo[1] = (i, currentCost)
            elif currentCost > worstTwo[0][1]:
                worstTwo[0] = (i, currentCost)
        return worstTwo

    def tournament_selection(self):
        """Select some amount of random tours and get the best from them."""
        tour_len = len(self.tours) - 1
        vals = [randint(0, tour_len) for x in range(self.tournament_size)]
        rand_tours = [self.tours[x] for x in vals]
        _, best_tuple = self.get_best_tours(rand_tours)

        return self.tours[best_tuple[0]]

    def mutate(self, tour):
        """Chance of performing slight random change to tour."""
        index1 = randint(0, len(tour.cities) - 1)
        index2 = randint(0, len(tour.cities) - 1)
        if random.random() < self.prob_mutation:
            tour.swap(index1, index2)
        return tour
