discovered=[]
def BFSWithAdjacencyList(adjacencyList):
    global discovered
    T=[]
    for i in range(len(adjacencyList)):
        if i not in discovered:
            T+=[breadthFirstWithAdjacencyList(adjacencyList,i)]
    return T

def breadthFirstWithAdjacencyList(adjacencyList,start):
    global discovered
    queue = [start]
    discovered += [start]
    edges=[]
    while(len(queue)!=0):
        for i in adjacencyList[queue[0]]:
            if(i not in discovered):
                #if the vertex hasn't been discovered
                discovered+=[i] #discover it
                queue+=[i] #add it to the queue
                edges+=[(queue[0],i)]
        queue.pop(0)
    return edges

print(BFSWithAdjacencyList([[1,2],[0,2],[0,1,3],[2]]))
