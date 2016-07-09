"""Tour.py."""
import math
import random


class Tour(object):
    """Represents a single path through all given nodes."""

    def __init__(self, lx, ly):
        """Initialize object."""
        self.x_points = lx
        self.y_points = ly
        self.cities = []
        self.distance = 0
        self.fitness = 0
        self.set_tour()

    def set_tour(self, city_list=None):
        """Set the ordered list of cities that represents this tour."""
        self.cities = city_list or \
            random.sample(range(len(self.x_points)), len(self.y_points))
        self.distance = 0
        self.fitness = 0

    def get_fitness(self):
        """Calculate and retreive fitness."""
        if self.fitness == 0:
            self.fitness = 1 / self.get_cost()
        return self.fitness

    def swap(self, index1, index2):
        """Swap two cities."""
        temp = self.cities[index1]
        self.cities[index1] = self.cities[index2]
        self.cities[index2] = temp
        # Reset distance calculation
        self.distance = 0
        self.fitness = 0

    def get_cost(self):
        """Calculate total distance of tour."""
        if self.distance == 0:
            for i in range(1, len(self.cities) + 1):
                point1 = self.cities[i - 1]
                point2 = self.cities[i % len(self.cities)]
                self.distance += self.distance_to(point1, point2)
        return self.distance

    def distance_to(self, point1, point2):
        """Distance formula between two points."""
        delta_x = self.x_points[point1] - self.x_points[point2]
        delta_y = self.y_points[point1] - self.y_points[point2]
        return math.sqrt(delta_x * delta_x + delta_y * delta_y)
