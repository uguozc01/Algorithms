def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances =  [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float("inf")) for idx in range(numberOfVertices)])
    minDistancesHeap.update(start, 0)

    while not minDistancesHeap.isEmpty():
        vertex, currentMinDistance = minDistancesHeap.remove()

        if currentMinDistance == float("inf"):
            break
        
        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)

    # return list(map(lambda x: -1 if x == float("inf") else x, minDistances))
    z = list(map(lambda x: -1 if x == float("inf") else x, minDistances))
    print(z)

class MinHeap:
    def __init__(self, array):
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) -2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) -1 , array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] <  heap[childOneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
    
    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx -1) // 2
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx -1) // 2
    
    # O(log(n)) time | O(1) space
    def remove(self):
        if self.isEmpty():
            return
        
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance
    
    def swap(self, i, j, heap):
        self.vertexMap[heap[i][0]] = j
        self.vertexMap[heap[j][0]] = i
        heap[i], heap[j] = heap[j], heap[i]

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)

edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
start = 0
dijkstrasAlgorithm(start, edges)