import math
import random
import numpy as np

X = set()
Y = set()
for i in range(10):
    X.add(random.randint(-50, 50))
    Y.add(random.randint(-50, 50))
X = list(X)
Y = list(Y)
if len(X) != len(Y):
    X = X[:min(len(X), len(Y))]
    Y = Y[:min(len(X), len(Y))]
X = np.array(X)
Y = np.array(Y)

def generate_population(size, k_boundaries, b_boundaries):
    lower_k_boundary, upper_k_boundary = k_boundaries
    lower_b_boundary, upper_b_boundary = b_boundaries

    population = []
    for i in range(size):
        individual = {
            "k": random.uniform(lower_k_boundary, upper_k_boundary),
            "b": random.uniform(lower_b_boundary, upper_b_boundary),
        }
        population.append(individual)

    return population
    

def apply_function(individual):
    k = individual["k"]
    b = individual["b"]
    return - (np.sum((Y - k * X - b)**2))
    
def choice_by_roulette(sorted_population, fitness_sum):
    offset = 0
    normalized_fitness_sum = fitness_sum

    lowest_fitness = apply_function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = apply_function(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual
def sort_population_by_fitness(population):
    return sorted(population, key=apply_function)


def crossover(individual_a, individual_b):
    ka = individual_a["k"]
    ba = individual_a["b"]

    kb = individual_b["k"]
    bb = individual_b["b"]

    return {"k": (ka + kb) / 2, "b": (ba + bb) / 2}


def mutate(individual):
    next_k = individual["k"] + random.uniform(-1, 1)
    next_b = individual["b"] + random.uniform(-1, 1)

    lower_boundary, upper_boundary = (-100, 100)

    # Guarantee we keep inside boundaries
    next_k = min(max(next_k, lower_boundary), upper_boundary)
    next_b = min(max(next_b, lower_boundary), upper_boundary)

    return {"k": next_k, "b": next_b}


def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(apply_function(individual) for individual in population)

    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        second_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation
    
generations = 500

population = generate_population(size=100, k_boundaries=(-100, 100), b_boundaries=(-100, 100))

i = 1
while True:

    if i == generations:
        break

    i += 1

    population = make_next_generation(population)

best_individual = sort_population_by_fitness(population)[-1]
print("\n🔬 FINAL RESULT")
print("X=", X, " Y=", Y)
print(best_individual, apply_function(best_individual))
print(np.polyfit(X, Y, deg=1))
