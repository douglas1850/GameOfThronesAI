#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Douglas O'Meara
A* search to find fastest path from his starting place and the Wall
Begins in Trader Town and prints fastest path to reach The Wall
"""

import networkx as nx
import game_of_nodes as main

print(list(nx.astar_path(main.graph, "Trader Town", "The Wall")))