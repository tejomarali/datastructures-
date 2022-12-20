"Insertion sort code"
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key= arr[i]
    j=i-1
    while key<arr[j] and j>=0:
     arr[j+1],arr[j] = arr[j],arr[j+1]
     j-=1
     arr[j+1] = key
  return arr


data_input= input("Enter elements: " )
list1 = [int(x) for x in data_input.split()]   
insertion_sort(list1)
print('Sorted elements are: ',list1)
