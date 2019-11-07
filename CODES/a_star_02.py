#defining maze
maze = [[1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1]]
# a ,b are instantaneous cordinates
#initially a=b=0
a = 0
b = 0
while(a!=4 and b!=4):
    #making instantaneous position with *
    maze[a][b] = '*'
    #now checking all the positions that are available from current location
