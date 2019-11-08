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
    if(t_d>t_l or t_d>t_r or t_d>t_u):
        a =a
        b= b
        #then t_d is not the least values of cost
    else:
        # then t_d is the least value
        b = b + 1
    if (t_r > t_l or t_r > t_u or t_r > t_d):
        a = a
        b = b
    else:
        a += 1
    if (t_l > t_u or t_l > t_r or t_l > t_d):
        a = a
        b = b
    else:
        a = a - 1

    if (t_u > t_l or t_u > t_r or t_r > t_d):
        a = a
        b = b
    else:
        b = b - 1
if(a==4 and b==4):
    maze[a][b]="*"

print(maze)




