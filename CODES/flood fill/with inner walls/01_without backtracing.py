from numpy import *
#creating maze with no walls.
m = array([[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,6,7,5,7,4,7,3,7,3,7,4,7,5,7,6,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,5,7,4,7,3,7,2,7,2,7,3,7,4,7,5,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,4,7,3,7,2,7,1,7,1,7,2,7,3,7,4,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,3,7,2,7,1,7,0,7,0,7,1,7,2,7,3,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,3,7,2,7,1,7,0,7,0,7,1,7,2,7,3,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,4,7,3,7,2,7,1,7,1,7,2,7,3,7,4,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,5,7,4,7,3,7,2,7,2,7,3,7,4,7,5,10],
           [10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10],
           [10,6,7,5,7,4,7,3,7,3,7,4,7,5,7,6,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]])

i = array([[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,6,7,5,10,4,7,3,7,3,10,4,10,5,7,6,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],#done till here
           [10,5,10,4,7,3,10,2,10,2,7,3,7,4,10,5,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,4,10,3,10,2,10,1,7,1,7,2,10,3,7,4,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,3,10,2,10,1,7,0,7,0,10,1,7,2,7,3,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,3,7,2,7,1,10,0,7,0,10,1,7,2,10,3,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,4,7,3,10,2,7,1,10,1,7,2,7,3,7,4,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,5,7,4,10,3,10,2,10,2,7,3,7,4,10,5,10],
           [10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10],
           [10,6,10,5,7,4,7,3,7,3,7,4,7,5,7,6,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]])

#sarting position is 1,1 .....x,y are positions in y and x direction.
x = y = 1
while(i[x][y]!=0):
    a = i[x][y]
    d = i[x+1][y]  #downward direction one unit
    u = i[x-1][y]  #upward direction   one unit
    l = i[x][y-1]  #left direction    one unit
    r = i[x][y+1]  #right direcion    one unit
    D = i[x+2][y]
    U = i[x-2][y]
    L = i[][]
    R = i[][]
    # now walls are to be checked
    if(d == 7):

