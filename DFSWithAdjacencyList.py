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
    stack = [start]
    discovered += [start]
    edges=[]
    while(len(stack)!=0):
        current=stack[0]
        stack.pop(0)
        for i in adjacencyList[current]:
            #go through each edge
            if(i not in discovered):
                #if the vertex hasn't been discovered
                discovered+=[i] #discover it
                edges+=[(current,i)] #add the edge
                edges+=depthFirstWithAdjacencyList(adjacencyList,i) #explore the node
    return edges

print(DFSWithAdjacencyList([[1,2],[0,2],[0,1,3],[2]]))
