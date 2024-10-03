l=[]
n=int(input("no of element"))
for i in range(n):
    l.append(int(input("enter element:")))
search=int(input())
low=0
high=n-1
while(low<=high):
    mid=low+high//2
    if search== l[mid]: 
       print("found at index:",mid)
       break
    elif search< l[mid]:
       high=mid-1
       print("found at index:",high)
       break
    elif search>l[mid]:
       low=mid+1
       print("found at index:",low)
       break
