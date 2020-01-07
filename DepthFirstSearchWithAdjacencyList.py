discovered=[]
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

print(depthFirstWithAdjacencyList([[1,2],[0,2],[0,1,3],[2]],0))
