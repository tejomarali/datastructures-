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
