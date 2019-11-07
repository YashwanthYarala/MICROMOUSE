from array import *

maze_potential =[[6,5,4,3,3,4,5,6],
                 [5,4,3,2,2,3,4,5],
                 [4,3,2,1,1,2,3,4],
                 [3,2,1,0,0,1,2,3],
                 [3,2,1,0,0,1,2,3],
                 [4,3,2,1,1,2,3,4],
                 [5,4,3,2,2,3,4,5],
                 [6,5,4,3,3,4,5,6]]
maze_path = [[6,5,4,3,3,4,5,6],
                 [5,4,3,2,2,3,4,5],
                 [4,3,2,1,1,2,3,4],
                 [3,2,1,0,0,1,2,3],
                 [3,2,1,0,0,1,2,3],
                 [4,3,2,1,1,2,3,4],
                 [5,4,3,2,2,3,4,5],
                 [6,5,4,3,3,4,5,6]]
p_x = 0
p_y = 0
#starting from first element
#p_x and p_y be the positions
def flood_fill():
    p_y = 0
    for p_x in range(7):
        if(maze_path[p_x][p_y]>maze_path[p_x+1][p_y]):
            #if yes we move down
            maze_potential[p_x+1][p_y]=9
        elif(maze_path[p_x][p_y]>maze_path[p_x][p_y+1]):
            maze_potential[p_x][p_y+1] = 9
            p_x = p_x-1
            p_y=p_y+1

    print(maze_potential)


flood_fill()




