import networkx as nx
import matplotlib.pyplot as plt
import sys

G = nx.DiGraph()

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
with open(filename, 'r') as file:
    content = file.read()
    lines = content.split('\n')

for line in lines:
    src, dsts = line.split(': ')
    dsts = dsts.split(' ')
    for dst in dsts:
        G.add_edge(src, dst)
        G.add_edge(dst, src)

# Takes some time
nx.draw(G, with_labels=True)
plt.show()
