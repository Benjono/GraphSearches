discovered=[]

def DFSWithAdjacencyList(adjacencyList):
    global discovered
    T=[]
    for i in range(len(adjacencyList)):
        if i not in discovered:
            T+=[depthFirstWithAdjacencyList(adjacencyList,i)]
    return T

def depthFirstWithAdjacencyList(adjacencyList,start):
    global discovered
    discovered += [start]
    edges=[]
    current=start
    for i in adjacencyList[current]:
        #go through each edge
        if(i not in discovered):
            #if the vertex hasn't been discovered
            edges+=[(current,i)] #add the edge
            edges+=depthFirstWithAdjacencyList(adjacencyList,i) #explore the node
    return edges

print(DFSWithAdjacencyList([[1,2],[0,2],[0,1,3],[2]]))
