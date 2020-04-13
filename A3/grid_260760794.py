from heapq import heappush as push,heappop as pop
import sys


def gen_figure(my_data,rows,cols):
    figure = {}

    for x in xrange(rows): 	
        for y in xrange(cols):

            val = int(my_data[x][y])
            
            i_d = x * cols + y
            
            figure[i_d] = []
            
            if rows > (x+val):
                figure[i_d].append((x + val) * cols + y)
            if 0 <= (x-val):
                figure[i_d].append((x - val) * cols + y)
            if cols > (y+val):
                figure[i_d].append((x * cols) + y + val)
            if 0 <= (y - val):
                figure[i_d].append((x * cols) + y - val)

    return figure


#Dijkstra
def traverse(figure,n,m):

    dis = [-1 for i in xrange(n*m)]
    
    q = []
    
    G = n * m - 1
    
    push(q,(0,0))
    
    dis[0] = 0
    
    while(len(q) > 0):
        
        d, v = pop(q)
        
        for u in figure[v]:
            
            if (dis[u] > d + 1) or -1 == dis[u]:
                
                dis[u] = d + 1
                
                if u == G:
                    return d + 1
                

                push(q,(dis[u],u))

    return dis[-1]



if __name__ == '__main__':
    
    rows, cols = [int(x) for x in sys.stdin.readline().split()]
    
    my_data = []

    for i in xrange(rows):
        my_data.append(sys.stdin.readline().strip())

    figure = gen_figure(my_data,rows,cols)
    
    print traverse(figure,rows,cols) 