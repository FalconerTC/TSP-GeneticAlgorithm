#!/usr/bin/env python

import math

import numpy as np
import matplotlib.pyplot as plt

from Genalgo import Genalgo
from Tour import Tour

def main():
    #make_plot_original([1,2,3,4], [1,5,9,16])
    lx, ly = parse_data('lib/xqf131.tsp')
    algo = Genalgo(lx, ly)
    algo.initialize()
    limit = 10000
    #print algo.crossover(algo.tours[0].cities, algo.tours[1].cities)
    #algo.evolve_new_pop()


    for i in range(0,limit):
         #algo.evolve_new_pop(i)
         algo.evolve_same_pop(i)
         if i == 10:
            _, best_tuple = algo.get_best_tours(algo.tours)
            best = algo.tours[best_tuple[0]]
            cities = best.cities
            cities.append(best.cities[0])
            make_plot_solved(lx, ly, cities)
            save_plot('solved-10.png')
         if i == 100:
            _, best_tuple = algo.get_best_tours(algo.tours)
            best = algo.tours[best_tuple[0]]
            cities = best.cities
            cities.append(best.cities[0])
            make_plot_solved(lx, ly, cities)
            save_plot('solved-100.png')
         if i == 1000:
            _, best_tuple = algo.get_best_tours(algo.tours)
            best = algo.tours[best_tuple[0]]
            cities = best.cities
            cities.append(best.cities[0])
            make_plot_solved(lx, ly, cities)
            save_plot('solved-1000.png')
         if i == 10000:
            _, best_tuple = algo.get_best_tours(algo.tours)
            best = algo.tours[best_tuple[0]]
            cities = best.cities
            cities.append(best.cities[0])
            make_plot_solved(lx, ly, cities)
            save_plot('solved-10000.png')
         pass

    _, best_tuple = algo.get_best_tours(algo.tours)
    best = algo.tours[best_tuple[0]]
    cities = best.cities
    cities.append(best.cities[0])
    print "Best: ",best.get_cost()

    make_plot_original(lx, ly)
    save_plot('original.png')
    make_plot_solved(lx, ly, cities)
    save_plot('solved.png')


def parse_data(name):
    with open(name) as f:
        lines = f.read().splitlines()
    lines = filter(lambda x: x.split(' ')[0].isdigit(), lines)
    lx = [int(p.split(' ')[1]) for p in lines]
    ly = [int(p.split(' ')[2]) for p in lines]
    return lx, ly

# Plot functions
def make_plot_original(lx, ly):
    plt.plot(lx, ly, 'ro');
    plt.axis([-5, max(lx)+5, -5, max(ly)+5])

def make_plot_solved(lx, ly, tour):
    make_plot_original(lx, ly)
    for i in range(1, len(tour)):
        p2 = tour[i]
        p1 = tour[i-1]
        plt.plot([lx[p1], lx[p2]], [ly[p1], ly[p2]], 'k-')

def save_plot(name):
    plt.savefig(name)

if __name__ == "__main__":
    main()
