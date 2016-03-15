#!/usr/bin/env python

import math

import numpy as np
import matplotlib.pyplot as plt

def main():
    print "hello"
    #make_plot_original([1,2,3,4], [1,5,9,16])
    lx, ly = parse_data('lib/xqf131.tsp')
    make_plot_original(lx, ly)
    #make_plot_solved([1, 2, 3, 4], [1, 5, 9, 16], [0, 3, 1, 2])
    save_plot('original.png')
    print distance([1, 1], [1, 4])
    

def parse_data(name):
    with open(name) as f:
        lines = f.read().splitlines()
    lines = filter(lambda x: x.split(' ')[0].isdigit(), lines)
    lx = [int(p.split(' ')[1]) for p in lines]
    ly = [int(p.split(' ')[2]) for p in lines]
    print lx, ly
    return lx, ly

# Helper functions
def distance(x, y):
    xd = x[0] - x[1]
    yd = y[0] - y[1]
    return round(math.sqrt(xd*xd + yd*yd))

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
