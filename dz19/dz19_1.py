import networkx as nx
import matplotlib.pyplot as plt

cities = []
with open("cities.csv") as file:
    for string in file:
        city1, city2, distance = string.strip().split(";")
        cities.append([city1, city2, distance])

print("Створено список типу cities =", cities)

g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight = int(edge[2]))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph of cities")
plt.show()
