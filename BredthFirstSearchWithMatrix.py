def breadthFirstWithMatrix(graphMatrix,start):
    queue = [start]
    discovered = [start]
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

print(breadthFirstWithMatrix([[0,1,1,0],[1,0,0,0],[1,0,0,1],[1,0,0,0]],0))
# [[0,1,1,1],
#  [0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0]]
                
