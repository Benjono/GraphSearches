discovered=[]

def DFSWithMatrix(graphMatrix):
    global discovered
    T=[]
    for i in range(len(graphMatrix)):
        if i not in discovered:
            T+=[depthFirstWithMatrix(graphMatrix,i)]
    return T


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

print(DFSWithMatrix([[0,1,1,0],[1,0,1,0],[1,1,0,1],[1,0,0,0]]))
