import networkx as nx

def file_graph(file_cities: str):
    cities = []
    with open("cities.csv") as file:
        for string in file:
            city1, city2, distance = string.split(";")
            cities.append([city1, city2, distance])
    return cities

def get_path(g, start_city, finish_city):
    path = nx.shortest_path(g, start_city, finish_city, weight="weight")
    dist = nx.shortest_path_length(g, start_city, finish_city, weight="weight")
    return path, dist

edge_cities = file_graph("cities.csv")
g = nx.Graph()

for edge in edge_cities:
    g.add_edge(edge[0], edge[1], weight=int(edge[2]))

path_1, dist_1 = get_path(g, "Chernihiv", "Simferopol")

print("Визначений маршрут:", *path_1, sep=" - " )
print("Протяжність маршруту:", dist_1)
