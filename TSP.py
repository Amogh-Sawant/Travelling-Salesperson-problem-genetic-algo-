import pygame
import random

height = 500
width = 500
window = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.display.set_caption("travelling salesperson")
fps = 300
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

def swap(a, b):
    temp = b 
    b = a
    a = temp
    return a, b

def mutate(town):
        random_range = random.randrange(0, len(town))
        for _ in range(random_range):
                city_x = random.randrange(0, len(town))
                city_y = random.randrange(0, len(town))
                if city_x != city_y:
                        town[city_x], town[city_y] = swap(town[city_x], town[city_y])
        return town 

def optimize(town): 
        pop = []
        pop_size = 100
        for _ in range(pop_size):
                town_copy = []
                for city in town:
                        town_copy.append(city)
                c = list(mutate(town_copy))
                c.append(total_distance(c))
                pop.append(c)

        pop.sort(key=lambda x: x[-1])
        best_town = pop[0]

        return best_town[:-1]

town = []
num_of_cities = 10
best_distance = 1_000_000_000
current_distance = 0
optimal_route = []
route_distance = []

for _ in range(num_of_cities):
    c = City(random.randint(0, width), random.randint(0, height))
    town.append(c)

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
    
    town = optimize(town)
    # random.shuffle(town)
        
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False 

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
