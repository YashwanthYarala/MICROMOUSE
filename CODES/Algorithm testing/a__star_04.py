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
print("test ok ")

a = 1
b = 1
h = k = 4
def cost(p,q):
    t = 1+abs(p-h)+abs(q-k)
    return t

while(a!=4 & b!=4):
    # checking the posibility of motion

    maze[a][b] = '*'
    if(maze[a+1][b]==1):   #checking for right
        t_r=cost(a+1,b)
    else:
        t_r = 100


    if(maze[a][b+1]==1):
        t_d = cost(a,b+1)
    else:
        t_d = 101
    if(maze[a-1][b]==1):
        t_l = cost(a-1,b)
    else:
        t_l = 102
    if(maze[a][b-1]==1):
       t_u = cost(a,b-1)
    else:
        t_u = 103

    #print(t_r,t_l,t_d,t_u)
# comparison between costs
    m = min(t_r,t_l,t_d,t_u)
    if(t_r==m):
        b = b+1
        a =a
        print("m")
    elif(t_d ==m):
        a +=1
        b=b
    elif (t_l ==m):
        b -=1
        a = a
    elif (t_u == m):
        a = a-1
        b =b




print(maze)





