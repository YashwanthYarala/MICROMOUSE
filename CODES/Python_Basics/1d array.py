# for loop
friends = ['yashwnth','reddy','yarala']
for x in friends:
    print(x)
    print(len(x))  #for each x it gives no.of elements in the x
for x in friends[:4]:
    print(x)
sum = 0
for x in range(10): #this range includes numbers from 0 t0 9
    sum +=x
    print(sum)
#functions
def func1(a,b):
    print(a+b)
func1(2,3)
#sets
marks = {"12","13","15","18","21","32","12"}  #it doesnt consider about repititions
print(marks)
#dictionary
#here we use keys and values instead of word and meaning respectively
classmates = {'tony':'good guy','stark':'intelligent'}
print(classmates['tony'])
for k,v in classmates.items():  #for looping we have to itterate both key and value
    print(k + v)







