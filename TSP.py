import pygame
import random
import numpy as np

height = 500
width = 500
window = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.display.set_caption("travelling salesperson")
fps = 5
clock = pygame.time.Clock()
run = True
pygame.init()

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.circle(window, white, (int(self.x), int(self.y)), 5)

    def draw_route(self, cityA, cityB):
        pygame.draw.line(window, white, cityA, cityB)


def distance(cityA, cityB):
    return ((abs(cityA[0]-cityB[0])**2) + (abs(cityA[1]-cityB[1])**2))**0.5

def total_distance(town):
    d = 0
    for j in range(len(town)):
        if j != len(town) - 1:
            cityA = (town[j].x, town[j].y)
            cityB = (town[j+1].x, town[j+1].y) 
            d += distance(cityA, cityB)
    return int(d)

def optimize(population):
    parent1 = []
    parent2 = []
    child = []
    new_gen = []
    distances = []
    population = np.array(population)
    population = population[population[:, 1].argsort()] 

    for i in range(len(population[0])):
        parent1 = population[0][0]
        parent2 = population[1][0]
    # print(population)
    print(f"parent1 ----------------------- {parent1}")
    print(f"parent2 ----------------------- {parent2}")
    for _ in range(population_size):
        child = parent1[:random.randint(0, len(parent1))]
    
        for gene in parent2:
            if gene not in child:
                child.append(gene)
        new_gen.append(child)

    for d in range(len(new_gen)):
        distances.append(total_distance(new_gen[d])) 

    return list(zip(new_gen, distances))

town = []
num_of_cities = 7
best_distance = 1_000_000_000
current_distance = 0
optimal_route = []
population_size = 10
population = []
route_distance = []

for _ in range(num_of_cities):
    c = City(random.randint(0, width), random.randint(0, height))
    town.append(c)

for _ in range(population_size):
    random.shuffle(town)
    route_distance.append(total_distance(town))

for t in town:
    optimal_route.append(t)

while run:
    window.fill(black)
    i = 0
    for city in optimal_route:
        city.draw()
        if i != (len(optimal_route)-1):
            cityA = (optimal_route[i].x, optimal_route[i].y)
            cityB = (optimal_route[i+1].x, optimal_route[i+1].y) 
            
            city.draw_route(cityA, cityB) 
        i += 1
    
    current_distance = total_distance(town) 
    if current_distance < best_distance:
        best_distance = current_distance
        optimal_route = []
        for t in town:
            optimal_route.append(t)
        print(best_distance)
    
    random.shuffle(town)
        
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False 

    pygame.display.update()
    clock.tick(fps)

# while run:
#     window.fill(black)
#     i = 0
#     for t in population[0][0]:
#         town.append(t)
#     for city in optimal_route:
#         city.draw()
#         if i != (len(optimal_route)-1):
#             cityA = (optimal_route[i].x, optimal_route[i].y)
#             cityB = (optimal_route[i+1].x, optimal_route[i+1].y) 
            
#             city.draw_route(cityA, cityB) 
#         i += 1
    
#     population = optimize(population)
#     current_distance = total_distance(town) 
#     if current_distance < best_distance:
#         best_distance = current_distance
#         optimal_route = []
#         for t in town:
#             optimal_route.append(t)
#         print(best_distance)
        
#     for event in pygame.event.get():
#         if event.type is pygame.QUIT:
#             run = False 

#     pygame.display.update()
#     clock.tick(fps)

pygame.quit()
quit()