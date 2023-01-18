import random

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Knapsack:
    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items
        self.value = sum([item.value for item in items])
        self.weight = sum([item.weight for item in items])

def generate_items(num_items):
    items = []
    for i in range(num_items):
        value = random.randint(2, 20)
        weight = random.randint(1, 10)
        items.append(Item(value, weight))
    return items

def generate_population(num_individuals, items):
    population = []
    for i in range(num_individuals):
        item = random.choice(items)
        knapsack = Knapsack(200, [item])
        population.append(knapsack)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1.items))
    child_items = parent1.items[:crossover_point] + parent2.items[crossover_point:]
    return Knapsack(200, child_items)

def mutation(individual, mutation_probability):
    if random.uniform(0, 1) < mutation_probability:
        item_to_remove = random.choice(individual.items)
        individual.items.remove(item_to_remove)
        new_item = random.choice(items)
        individual.items.append(new_item)

def local_improvement(individual, items):
    knapsack_items = individual.items.copy()
    current_weight = individual.weight
    current_value = individual.value

    for item in items:
        if current_weight + item.weight <= 200:
            knapsack_items.append(item)
            current_weight += item.weight
            current_value += item.value
    individual.items = knapsack_items
    individual.weight = current_weight
    individual.value = current_value


def print_population(population):
    for i, knapsack in enumerate(population):
        print("Knapsack {}: weight = {}, value = {}".format(i+1, knapsack.weight, knapsack.value))

def print_knapsack(knapsack):
    print("Knapsack : weight = {}, value = {}".format(knapsack.weight, knapsack.value))

if __name__ == "__main__":
    generations_number = int(input('Enter number of generations: '))
    items = generate_items(100)
    population = generate_population(100, items)

    for generation in range(generations_number):
        new_population = []
        for i in range(100):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutation(child, 0.1)
            local_improvement(child, items)
            new_population.append(child)
        population = new_population
    total_fitness = sum([knapsack.value for knapsack in population])
    mean_fitness = int(total_fitness / len(population))
    max_fitness = max(population, key=lambda x: x.value)

    best_individual = max(population, key=lambda x: x.value)
    print_knapsack(best_individual)
    print("Best knapsack value:", best_individual.value)
    print("Mean fitness:", mean_fitness)
    print("Max fitness:", max_fitness.value)
    print("Knapsack items: ")
    for item in best_individual.items:
        print(f"Item: value = {item.value},\tweight = {item.weight}")


