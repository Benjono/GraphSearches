discovered=[]
def depthFirstWithMatrix(graphMatrix,start):
    global discovered
    discovered += [start]
    edges=[]
    current=start
    for i in range(len(graphMatrix)):
        #go through each potential edge
        #determining adjacency takes O(n) time
        if(graphMatrix[current][i]==1):
            #if there is an edge
            if(i not in discovered):
                #if the vertex hasn't been discovered
                edges+=[(current,i)]
                edges+=depthFirstWithMatrix(graphMatrix,i)
    return edges

print(depthFirstWithMatrix([[0,1,1,0],[1,0,1,0],[1,1,0,1],[1,0,0,0]],0))
