#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Douglas O'Meara
Breadth first search"
Start at The Wall, print sequence of cities to reach every city as efficiently as possible
"""
import networkx as nx
import csv


keys = []
d = {}
adjacent = {}
#create nodes
with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    G = nx.Graph()
        
    
    for row in plots:
        if row[1].isdigit():
            keys.append(row[0])
            d.setdefault(row[0], []).append(int(row[1]))
            d.setdefault(row[0], []).append(int(row[2]))
        else: #is an edge
            adjacent.setdefault(row[0], []).append(row[1])
            adjacent.setdefault(row[1], []).append(row[0])
            
#here for testing
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

#print(generate_edges(adjacent))
edges = generate_edges(adjacent)


def conquer_the_world(graph, start):
    #track all visited nodes
    explored = []
    #"The Wall" only value in queue initially
    queue = [start]
    # keep looping while there are nodes still to be checked
    while queue:
        # pop first node from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    #explored is array of cities visited in the order they were visited
    return explored

print(conquer_the_world(adjacent,'The Wall'))