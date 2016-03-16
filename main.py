#!/usr/bin/env python

import math

import numpy as np
import matplotlib.pyplot as plt

from Genalgo import Genalgo

def main():
    #make_plot_original([1,2,3,4], [1,5,9,16])
    lx, ly = parse_data('lib/xqf131.tsp')
    algo = Genalgo(lx, ly)
    algo.initialize()
    limit = 1000
    #print algo.crossover(algo.tours[0].cities, algo.tours[1].cities)
   

    #for i in range(0, limit)
    #    solution = algo.evolve()

    for i in range(0,limit):
         algo.evolve_same_pop()

    best = algo.get_best_tours(algo.tours)

    algo.tours[best[1][0]].cities.append(algo.tours[best[1][0]].cities[0])
    print  algo.tours[best[1][0]].cities
    #make_plot_original(lx, ly)
    make_plot_solved(lx, ly, algo.tours[best[1][0]].cities)
    save_plot('original.png')


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
