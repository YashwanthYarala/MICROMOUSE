from array import *

maze_potential =[[6,5,4,3,3,4,5,6],
                 [5,4,3,2,2,3,4,5],
                 [4,3,2,1,1,2,3,4],
                 [3,2,1,0,0,1,2,3],
                 [3,2,1,0,0,1,2,3],
                 [4,3,2,1,1,2,3,4],
                 [5,4,3,2,2,3,4,5],
                 [6,5,4,3,3,4,5,6]]
maze_path = maze_potential
for i in range(8):
    for j in range(8):
