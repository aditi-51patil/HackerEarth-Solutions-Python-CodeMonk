n,m,g = input().split()
t =[int(i) for i in input().split()] # rains timing
a= [int(i) for i in input().split()] #Clothes dry time
count=0
a_win = [y-x for x,y in zip(t,t[1:])]
max_time=max(a_win)
for i in range(len(a)):
    if(a[i]<=max_time):
        # a[i] = 100000000
        count+=1
print(count)