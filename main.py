#!/usr/bin/env python
"""main.py."""
import matplotlib.pyplot as plt

from Genalgo import Genalgo


def main():
    """Manage simulation and save results."""
    test_file = 'lib/pbk411.tsp'
    limit = 1000
    milestones = [10, 25, 100, 500, 1000]

    lx, ly = parse_data(test_file)
    algo = Genalgo(lx, ly)
    current = 0

    for i in range(0, limit):
        algo.evolve_new_pop(i)
        if i == milestones[current]:
            cities, distance = get_best(algo)
            cities.append(cities[0])
            make_plot_solved(lx, ly, cities)
            save_plot('solved-' + str(milestones[current]) + '.png')
            print(str(milestones[current]) + ': ' + str(distance))
            current += 1

    _, best_tuple = algo.get_best_tours(algo.tours)
    best = algo.tours[best_tuple[0]]
    cities = best.cities
    cities.append(best.cities[0])
    print('Best: ' + str(best.get_cost()))

    make_plot_original(lx, ly)
    save_plot('original.png')
    make_plot_solved(lx, ly, cities)
    save_plot('solved.png')


def get_best(algo):
    """Get the best cities and their costs."""
    _, best_tuple = algo.get_best_tours(algo.tours)
    best = algo.tours[best_tuple[0]]
    cities = []
    for i in best.cities:
        cities.append(i)
    return cities, best.get_cost()


def parse_data(name):
    """Parse example data into x, y values."""
    with open(name) as f:
        lines = f.read().splitlines()
    lines = filter(lambda x: x.split(' ')[0].isdigit(), lines)
    lx = [int(p.split(' ')[1]) for p in lines]
    ly = [int(p.split(' ')[2]) for p in lines]
    return lx, ly


def make_plot_original(lx, ly):
    """Plot graph without traversal."""
    plt.plot(lx, ly, 'ro')
    plt.axis([-5, max(lx) + 5, -5, max(ly) + 5])


def make_plot_solved(lx, ly, tour):
    """Plot graph with given solution."""
    make_plot_original(lx, ly)
    for i in range(1, len(tour)):
        p2 = tour[i]
        p1 = tour[i - 1]
        plt.plot([lx[p1], lx[p2]], [ly[p1], ly[p2]], 'k-')


def save_plot(name):
    """Save graph to disk."""
    plt.savefig(name)
    plt.clf()

if __name__ == "__main__":
    main()
