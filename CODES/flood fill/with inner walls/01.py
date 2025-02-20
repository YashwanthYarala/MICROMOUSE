from numpy import *
#creating maze with no walls.
m = array([[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,6,7,5,7,4,7,3,7,3,7,4,7,5,7,6,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,5,7,4,7,3,7,2,7,2,7,3,7,4,7,5,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,4,7,3,7,2,7,1,7,1,7,2,7,3,7,4,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,3,7,2,7,1,7,0,7,0,7,1,7,2,7,3,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,3,7,2,7,1,7,0,7,0,7,1,7,2,7,3,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,4,7,3,7,2,7,1,7,1,7,2,7,3,7,4,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,5,7,4,7,3,7,2,7,2,7,3,7,4,7,5,10,10],
           [10,10,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,10,10],
           [10,10,6,7,5,7,4,7,3,7,3,7,4,7,5,7,6,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]])

i = array([[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,6,7,5,10,4,7,3,7,3,10,4,10,5,7,6,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],#done till here
           [10,10,5,10,4,7,3,10,2,10,2,7,3,7,4,10,5,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,4,10,3,10,2,10,1,7,1,7,2,10,3,7,4,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,3,10,2,10,1,7,0,7,0,10,1,7,2,7,3,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,3,7,2,7,1,10,0,7,0,10,1,7,2,10,3,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,4,7,3,10,2,7,1,10,1,7,2,7,3,7,4,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,5,7,4,10,3,10,2,10,2,7,3,7,4,10,5,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,6,10,5,7,4,7,3,7,3,7,4,7,5,7,6,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]])
w= array([[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,6,7,5,10,4,7,3,7,3,10,4,10,5,7,6,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],#done till here
           [10,10,5,10,4,7,3,10,2,10,2,7,3,7,4,10,5,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,4,10,3,10,2,10,1,7,1,7,2,10,3,7,4,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,3,10,2,10,1,7,0,7,0,10,1,7,2,7,3,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,3,7,2,7,1,10,0,7,0,10,1,7,2,10,3,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,4,7,3,10,2,7,1,10,1,7,2,7,3,7,4,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,5,7,4,10,3,10,2,10,2,7,3,7,4,10,5,10,10],
           [10,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,7,10,10],
           [10,10,6,10,5,7,4,7,3,7,3,7,4,7,5,7,6,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
           [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]])

#sarting position is 1,1 .....x,y are positions in y and x direction.
x = y = 2
while(i[x][y]!=0):
    w[x][y] = 9
    a = i[x][y]
    d = i[x+1][y]  #downward direction one unit
    u = i[x-1][y]  #upward direction   one unit
    l = i[x][y-1]  #left direction    one unit
    r = i[x][y+1]  #right direcion    one unit
    D = i[x+2][y]  #downward 2 units
    U = i[x-2][y]  # upward  2 units
    L = i[x][y-2]  #left 2 units
    R = i[x][y+2]  #right 2 units
    # sorting the cell values.
    val = [D,R,L,U]
    asc = array((sorted(set(val))))
    print(asc)# arranging the values in ascending order.
    print(asc[0],asc[1])
    l1 = asc.size
    print(l1)
    p = 0
    while(p<l1):      # to get the number of elements in the sorted array excluding 10
        #print("working")
        if(asc[p]==10):
            l1 = l1-1
        p = p+1

    # now walls are to be checked
    t = min(d,l,u,r)


    if(l1 == 4):
        a = x
        b = y
        if(d == t):
            if(D == asc[0]):
                x +=2

        elif(r == t):
            if(R == asc[0]):
                y+=2

        elif( u == t):
            if(U == asc[0]):
                x = x-2

        elif( l == t):
            if(L == asc[0]):
                y =y-2
        if(a==x and b == y):
            if (d == t):
                if (D == asc[1]):
                    x += 2

            elif (r == t):
                if (R == asc[1]):
                    y += 2

            elif (u == t):
                if (U == asc[1]):
                    x = x - 2

            elif (l == t):
                if (L == asc[1]):
                    y = y - 2
        if(a == x and b == y):
            if (d == t):
                if (D == asc[2]):
                    x += 2

            elif (r == t):
                if (R == asc[2]):
                    y += 2

            elif (u == t):
                if (U == asc[2]):
                    x = x - 2

            elif (l == t):
                if (L == asc[2]):
                    y = y - 2
        if(a == x and b == y):
            if (d == t):
                if (D == asc[3]):
                    x += 2

            elif (r == t):
                if (R == asc[3]):
                    y += 2

            elif (u == t):
                if (U == asc[3]):
                    x = x - 2

            elif (l == t):
                if (L == asc[3]):
                    y = y - 2
    elif  (l1 == 3):
        a = x
        b = y
        if(d == t):
            if(D == asc[0]):
                x +=2

        elif(r == t):
            if(R == asc[0]):
                y+=2

        elif( u == t):
            if(U == asc[0]):
                x = x-2

        elif( l == t):
            if(L == asc[0]):
                y =y-2
        if(a==x and b == y):
            if (d == t):
                if (D == asc[1]):
                    x += 2

            elif (r == t):
                if (R == asc[1]):
                    y += 2

            elif (u == t):
                if (U == asc[1]):
                    x = x - 2

            elif (l == t):
                if (L == asc[1]):
                    y = y - 2
        if(a == x and b == y):
            if (d == t):
                if (D == asc[2]):
                    x += 2

            elif (r == t):
                if (R == asc[2]):
                    y += 2

            elif (u == t):
                if (U == asc[2]):
                    x = x - 2

            elif (l == t):
                if (L == asc[2]):
                    y = y - 2
    elif(l1 == 2):
        a = x
        b = y
        if (d == t):
            if (D == asc[0]):
                x += 2

        elif (r == t):
            if (R == asc[0]):
                y += 2

        elif (u == t):
            if (U == asc[0]):
                x = x - 2

        elif (l == t):
            if (L == asc[0]):
                y = y - 2
        print(a,b,x,y)
        if (a == x and b == y):

            if (d == t):
                if (D == asc[1]):
                    x += 2

            elif (r == t):
                if (R == asc[1]):
                    y += 2

            elif (u == t):
                if (U == asc[1]):
                    x = x - 2

            elif (l == t):
                if (L == asc[1]):
                    y = y - 2
    elif(l1 == 1):
        a = x
        b = y
        if (d == t):
            if (D == asc[0]):
                x += 2

        elif (r == t):
            if (R == asc[0]):
                y += 2

        elif (u == t):
            if (U == asc[0]):
                x = x - 2

        elif (l == t):
            if (L == asc[0]):
                y = y - 2
    print("a , b" ,a,b)
    print("x , y",x,y)





















