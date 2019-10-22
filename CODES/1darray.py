from array import *
vals = array('i',[5,-6,3,5]) #this is like array(data type,data of the array)
print(vals)
print(vals.buffer_info())
for i in range(4):
    print(vals[i])
for e in range(len(vals)):
    print(vals[i])
for e in vals:
    print(e)