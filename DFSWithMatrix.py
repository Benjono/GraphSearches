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
    stack = [start]
    discovered += [start]
    edges=[]
    while(len(stack)!=0):
        current=stack[0]
        stack.pop(0)
        for i in range(len(graphMatrix)):
            #go through each potential edge
            #determining adjacency takes O(n) time
            if(graphMatrix[current][i]==1):
                #if there is an edge
                if(i not in discovered):
                    #if the vertex hasn't been discovered
                    discovered+=[i] #discover it
                    edges+=[(current,i)]
                    edges+=depthFirstWithMatrix(graphMatrix,i)
    return edges

print(DFSWithMatrix([[0,1,1,0],[1,0,1,0],[1,1,0,1],[1,0,0,0]]))
