discovered = []
def BFSWithMatrix(graphMatrix):
    global discovered
    T=[]
    for i in range(len(graphMatrix)):
        if i not in discovered:
            T+=[breadthFirstWithMatrix(graphMatrix,i)]
    return T
def breadthFirstWithMatrix(graphMatrix,start):
    global discovered
    queue = [start]
    discovered += [start]
    edges=[]
    while(len(queue)!=0):
        for i in range(len(graphMatrix)):
            #go through each potential edge
            #determining adjacency takes O(n) time
            if(graphMatrix[queue[0]][i]==1):
                #if there is an edge
                if(i not in discovered):
                    #if the vertex hasn't been discovered
                    discovered+=[i] #discover it
                    queue+=[i] #add it to the queue
                    edges+=[(queue[0],i)]
        queue.pop(0)
    return edges

print(BFSWithMatrix([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]))
# [[0,1,1,1],
#  [0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0]]
                
