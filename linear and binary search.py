"linear search code:"
def linear_search(lst, ele):
    for i in range(len(lst)):
        if (ele == lst[i]): 
            print("",i)
            break

    else :
      print('-1')

lst1 = []
n = int(input(''))
for k in range(0, n):
  num = int(input())
  lst1.append(num)
print(lst1)
 
ele = int(input(''))
linear_search(lst1,ele)


"binary search code :"
    
def binary_search(arr,x,low,high):
  if (low<=high):
    mid = (low+high)//2
    if(arr[mid] == x):
      return mid

    elif arr[mid] > x:
      return binary_search(arr,x,low,mid-1)
    else:
      return binary_search(arr,x,mid+1,high)
  else:
    return -1 

str_input= input( )
list1 = [int(x) for x in str_input.split()] 
y = int(input())

res = binary_search(list1,y,0,len(list1)-1)
if(res!=-1):
  print("",str(res))
else:
  print(-1)         

    
