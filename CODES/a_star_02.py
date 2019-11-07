#defining maze
# preference of moving right > down > left > up
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
a = 7
b = 7
# h ,k are final positions ,h=k=4
h = 4
k = 4
while(a!=4 and b!=4):
    #making instantaneous position with *
    maze[a][b] = '*'
    #now checking all the positions that are available from current location
    #We have to check the border conditions for indices of matrix
    if (a==7 or b==7):
        if(a==7 and b==7):
            # then it has only to positions to move either up or left
            # calculating the values of the next positions
            # and also the normal positions next to the present positions have to be checked
            #checking up conditon
            if (maze[a][b-1] == 1):
                # slot available to move
                g = 1
                p = abs(h-a)+abs(b-1-k)
                t_u = g+p
                b = b-1

            else:
                a =a-1



