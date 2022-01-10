from math import sqrt, inf
import matplotlib.pyplot as plt
import csv

def nn(V,C,u):
    # Starting point/node u, and tagged as 'N' = nezpracovany, points/nodes of Hamiltonian path, W as lenght of Hamiltonian path
    start = u
    S = ['N'] * len(V)
    Q = []
    Q.append(u) 
    W = 0
    # Choosen node u tagged as 'O' = otevreny
    S[u] = 'O'
    # Until nezpracovany node exist do:
    while 'N' in S:
        # Initialize minimal lenght of W
        minW = inf
        for v in V:
            # Get nezpracovany node as v
            if S[v] == 'N':
                # Distance between u and v
                dist = sqrt((C[u][0]-C[v][0])**2 + (C[u][1]-C[v][1])**2)
                # setting new minimum distance
                if dist < minW:
                    minW = dist
                    nn = v        
        # Adding nearest node to the path
        Q.append(nn)
        # Setting nearest node as new u
        u = nn
        S[u] = 'O'
        # add distance between u and v to W of Hamiltonian path
        W = W + minW
    # Closing Hamiltonian path
    dist_to_start = sqrt((C[u][0]-C[start][0])**2 + (C[u][1]-C[start][1])**2)
    Q.append(start)
    W = W + dist_to_start
    # returning Hamiltonian path as Q and its lenght as W
    return Q, W

# Function to show Hamiltonian path
def plot(Q,C):
    x = []
    y = []
    for u in Q:
        x.append(C[u][0])
        y.append(C[u][1])
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()

# Initializing data, coordinates of V -> C (dictionary), nodes -> V (list)
C = {}
V = []

# Loading data from csv file 
with open('data//airports.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        V.append(int(row[0]))
        C[int(row[0])] = [float(row[1]),float(row[2])]

#setting starting point
u = 0
Q, W = nn(V,C,u)
plot(Q, C)
print(W, Q)