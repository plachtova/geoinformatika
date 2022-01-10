from math import sqrt, inf
import matplotlib.pyplot as plt
import csv, random, copy

def BestInsertion(V,C):
# Starting point/node u, and tagged as 'N' = nezpracovany, points/nodes of Hamiltonian path, W as lenght of Hamiltonian path
    S = ['N'] * len(V)
    W = 0
    Q = []
    V_copy = copy.copy(V)
    # Choosing 3 random nodes from queue of nodes and putting to list
    start = random.sample(range(len(V_copy)),3)
    # Setting of 3 starting nodes as 'O' otevreny
    for i in range(3):
        S[start[i]] = 'O'
        # Calculating distance W of startig path
        if i+1 < 3:
            dist = sqrt((C[start[i]][0]-C[start[i+1]][0])**2 + (C[start[i]][1]-C[start[i+1]][1])**2)
            W = W + dist
        else:
            dist = sqrt((C[start[i]][0]-C[start[0]][0])**2 + (C[start[i]][1]-C[start[0]][1])**2)
            W = W + dist
        # Removing visited nodes from queue
        V_copy.remove(start[i])
        # Adding picked starting points to Hamiltonian path
        Q.append(start[i])
    
    # Until there is 'neotevreny' node:
    while 'N' in S:
        # Getting random 'neotevreny' node
        u = random.choice(V_copy)
        # Initializing minimal lenght of W
        minW = inf
        # Calculating distance between v1 u v2
        for j in range(len(Q)):
            v1 = Q[j]
            if j+1 < len(Q):
                v2 = Q[j+1]
            else:
                v2 = Q[0]
            new_dist = (sqrt((C[u][0]-C[v1][0])**2 + (C[u][1]-C[v1][1])**2) + sqrt((C[u][0]-C[v2][0])**2 + (C[u][1]-C[v2][1])**2) - sqrt((C[v1][0]-C[v2][0])**2 + (C[v1][1]-C[v2][1])**2))
            # If between v1 u v2 is minimum, set it as minW and mark place, where can be possibly added node to Hamiltonian path
            if new_dist < minW:
                minW = new_dist
                new_node = j+1
        # Setting node u as 'otevreny'
        S[u] = 'O'
        # Insert node to Hamiltonian path
        Q.insert(new_node, u)
        # Removing added node form queue
        V_copy.remove(u)
        # Adding minimum distance between v1 u v2 to W of Hamiltonian path
        W = W + minW
    # Closing Hamiltonian path
    Q.append(Q[0])
    return Q, W

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

# Loading data from .csv 
with open('data//airports.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        V.append(int(row[0]))
        C[int(row[0])] = [float(row[1]),float(row[2])]

Q, W = BestInsertion(V,C)
print(W, Q)
plot(Q, C)