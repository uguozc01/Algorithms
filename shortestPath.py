'''
You will be given an adjacency list and it represents a graph. The number of 
vertices in the graph is equal to the lenght of edges, where each index i in edges 
contains vertex i's outboung edges, in no particular order. Each individual edge is
represented by a pair of two numbers, [destination, distance], where destination is
a positive integer denoting the destination vertex and the distance is a positive integer 
representing the length of the edge( the distance from vertex i to vertex detination)
Note that these edges are directed so you can only travel from a particular vertex to 
its destination - not the other way around.

Write a function that computes the lenghts of the shortest path between start and 
all of the other vertices in the graph using Dijktras's algorithm and returns an array.
each index i in the output array should represent the length of the shortest path between
start and vertex i. If no path is found from start to vertex i then output[i] should be -1
'''

# O(V^2 + e) time | O(V) space 
# where v is the number of vertices and e is the number of edges
def shortestPath(start, edges):
    numberOfNodes = len(edges)

    minDistances =  [float("inf") for _ in range(numberOfNodes)]
    minDistances[start] = 0
    visited = set()

    while len(visited) != numberOfNodes:
        node, currentMinDistance = getnodeWithMinDistance(minDistances, visited)

        if currentMinDistance == float("inf"):
            break
        
        visited.add(node)

        for edge in edges[node]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue
            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))

def getnodeWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    node = None

    for nodeIdx, distance in enumerate(distances):
        if nodeIdx in visited:
            continue
        if distance <= currentMinDistance:
            node = nodeIdx
            currentMinDistance = distance
    return node, currentMinDistance

