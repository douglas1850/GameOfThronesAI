# -*- coding: utf-8 -*-
"""
Douglas O'Meara
Plot Westeros and the distance between each location
"""
import matplotlib.pyplot as plt
import csv
import networkx as nx
#import jon_snow_search.py

x = []
y = []

csvfile = open("data.csv", "r")
plots = csv.reader(csvfile, delimiter = ',')
G = nx.Graph()
plt.figure(figsize=(15,15))
    
for row in plots:
    if row[1].isdigit():
        G.add_node(row[0], point=(int(row[1]), int(row[2])))
    else: #is an edge
        G.add_edge(row[0], row[1], distance = row[2])


graph = nx.get_node_attributes(G, 'point')
edge = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx(G, graph, node_size = 5, font_size = 13)
nx.draw_networkx_edge_labels(G, graph, edge_labels = edge)
plt.show()