selesction sort code:
  
def selection_sort(arr,length):
  for i in range(length):
    cur_min = i

    for j in range(i+1, length):

      if arr[j]<arr[cur_min]:
         cur_min = j
    arr[i], arr[cur_min] = arr[cur_min], arr[i]
  return arr

data_input= input('enter numbers : ' )
list1 = [int(x) for x in data_input.split()] 
length = len(list1)
result= selection_sort(list1,length)
print("sorted elements are: " , result)  
