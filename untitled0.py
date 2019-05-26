# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:39:20 2019

@author: ayush
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections

df = pd.read_table("scheme 2 - 3.csv",sep=',',header=None)
A=np.array(df)
G=nx.from_numpy_array(A)
nx.draw(G,with_labels = True)
plt.show()

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

