import itertools
import random
import math

# Travelling Salesman Problem (TSP) - 3 Solution Approaches

def format_distance(dist):
    """Format distance to 2 decimal points."""
    return f"{dist:.2f}"
# Example set of cities (coordinates)
cities = {
    'A': (0, 0),
    'B': (1, 5),
    'C': (5, 2),
    'D': (6, 6)
}

def distance(city1, city2):
    """Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# 1. Brute Force Solution
def tsp_brute_force(cities):
    """Try all possible permutations to find the shortest tour."""
    city_list = list(cities.keys())
    min_path = None
    min_dist = float('inf')
    for perm in itertools.permutations(city_list):
        # Complete the cycle by returning to the start
        path = perm + (perm[0],)
        dist = sum(distance(path[i], path[i+1]) for i in range(len(cities)))
        if dist < min_dist:
            min_dist = dist
            min_path = path
    return min_path, min_dist

# 2. Nearest Neighbor Heuristic
def tsp_nearest_neighbor(cities, start):
    """At each step, visit the nearest unvisited city."""
    unvisited = set(cities.keys())
    path = [start]
    unvisited.remove(start)
    current = start
    total_dist = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        total_dist += distance(current, next_city)
        path.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    # Return to start
    total_dist += distance(current, start)
    path.append(start)
    return path, total_dist

# 3. Genetic Algorithm (Simple Version)
def tsp_genetic_algorithm(cities, population_size=10, generations=100, mutation_rate=0.1):
    """Use a genetic algorithm to approximate the shortest tour."""
    city_list = list(cities.keys())
    def create_individual():
        individual = city_list[:]
        random.shuffle(individual)
        return individual

    def fitness(individual):
        path = individual + [individual[0]]
        return 1 / sum(distance(path[i], path[i+1]) for i in range(len(cities)))

    def crossover(parent1, parent2):
        # Ordered crossover
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None]*len(parent1)
        child[start:end] = parent1[start:end]
        fill = [c for c in parent2 if c not in child]
        idx = 0
        for i in range(len(child)):
            if child[i] is None:
                child[i] = fill[idx]
                idx += 1
        return child

    def mutate(individual):
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(individual)), 2)
            individual[i], individual[j] = individual[j], individual[i]

    # Initialize population
    population = [create_individual() for _ in range(population_size)]
    for gen in range(generations):
        # Evaluate fitness
        population.sort(key=lambda ind: -fitness(ind))
        # Elitism: keep the best
        next_gen = population[:2]
        # Generate new individuals
        while len(next_gen) < population_size:
            parents = random.sample(population[:5], 2)
            child = crossover(parents[0], parents[1])
            mutate(child)
            next_gen.append(child)
        population = next_gen
    best = population[0]
    best_path = best + [best[0]]
    best_dist = sum(distance(best_path[i], best_path[i+1]) for i in range(len(cities)))
    return best_path, best_dist

# --- Example Usage ---

print("Cities:", cities)

# 1. Brute Force
path, dist = tsp_brute_force(cities)
print("\nBrute Force Solution:")
print("Path:", path)
print("Distance:", dist)

# 2. Nearest Neighbor (starting from 'A')
path, dist = tsp_nearest_neighbor(cities, 'A')
print("\nNearest Neighbor Solution:")
print("Path:", path)
print("Distance:", dist)

# 3. Genetic Algorithm
path, dist = tsp_genetic_algorithm(cities)
print("\nGenetic Algorithm Solution:")
print("Path:", path)
print("Distance:", dist)

# --- 
# Comments:
# - Brute Force tries every possible route (factorial time), always finds the best.
# - Nearest Neighbor is fast but can miss the optimal path.
# - Genetic Algorithm uses evolution-inspired search to find a good (not always optimal) solution.