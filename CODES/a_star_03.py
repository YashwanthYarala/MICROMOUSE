maze = [[0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]
# we start at (1,1)
a = 1
b = 1
h = k = 4
def cost(p,q):
    t = 1+abs(p-h)+abs(q-k)
    return t

while(a!=4 and b!=4):
    # checking the posibility of motion
    maze[a][b] = '*'
    if(maze[a+1][b]==1):   #checking for right
        t_r=cost(a+1,b)
    else:
        t_r = cost(a,b)
    if(maze[a][b+1]==1):
        t_d = cost(a,b+1)
    else:
        t_d = cost(a,b)
    if(maze[a-1][b]==1):
        t_l = cost(a-1,b)
    else:
        t_l = cost(a,b)
    if(maze[a][b-1]==1):
        t_u = cost(a,b-1)
    else:
        t_u = cost(a,b)
# comparison between costs




