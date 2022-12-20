"Bubble sorting code:"
def bubble_sort(list):
  for num in range(len(list)):
    for i in range(0, len(list) - num - 1):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1], list[i]
  return list
str_input= input( )
list = [int(x) for x in str_input.split()]

bubble_sort(list)
print('sorted elements are: ')
print(list)
