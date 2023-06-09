import itertools
import math

def tsp_force(start_city, cities):
    permutations = list(itertools.permutations(cities))
    min_distance = float('inf')
    optimal_route = None
    
    for permutation in permutations:
        distance = calculate_tdistance(permutation,start_city)
        
        if distance < min_distance:
            min_distance = distance
            optimal_route = permutation
                
    return optimal_route, min_distance

def calculate_tdistance(route,start_city):
    distance = 0
    
    distance += distance_bw_cities(start_city, route[0])
    
    for i in range(len(route)-1):
        distance += distance_bw_cities(route[i],route[i+1])
    distance += distance_bw_cities(route[-1], start_city)
    return distance

def distance_bw_cities(city1, city2):
    # Euclidean distance formula
    distance = math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)
    return distance

cities = [(0, 0), (1, 3), (4, 0), (2, 1)]
start_city = (0, 0)
optimal_route, min_distance = tsp_force(start_city, cities)
print("Optimal Route:", optimal_route)
print("Min Distance:", min_distance)

    