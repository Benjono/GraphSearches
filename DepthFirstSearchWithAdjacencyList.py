discovered=[]
def depthFirstWithMatrix(adjacencyMatrix,start):
    global discovered
    stack = [start]
    discovered += [start]
    edges=[]
    while(len(stack)!=0):
        current=stack[0]
        stack.pop(0)
        for i in adjacencyMatrix[current]:
            #go through each edge
            if(i not in discovered):
                #if the vertex hasn't been discovered
                discovered+=[i] #discover it
                edges+=[(current,i)] #add the edge
                edges+=depthFirstWithMatrix(adjacencyMatrix,i) #explore the node
    return edges

print(depthFirstWithMatrix([[1,2],[0,2],[0,1,3],[2]],0))
