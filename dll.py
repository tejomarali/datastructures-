'''doubly linked list:
        operations performed:
        1. insert at beginning
        2, insert at end
        3.insert at specific position
        4.delete at begin
        5. delete at end
        6. delete at specific position
        7. search 
        8. count
        9. display '''
class Node:
  def __init__(self, data):
    self.prev = None
    self.data = data
    self.next = None
class DLinkedList:
  def __init__(self):
    self.head = None
  def insertbegin(self, data):
    new_node = Node(data)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node
    self.head = new_node
   def insertlast(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node
    new_node.prev = last
   def insertrandom(self, data, pos):
    new_node = Node(data)
    temp = self.head
    for i in range(pos):
      if temp is None:
        print('error-x001')
        return
      ptr = temp
      temp = temp.next
     new_node.next = temp
    temp.prev = new_node
    ptr.next = new_node
    new_node.prev = ptr
   def deletebegin(self):
      if self.head is None:
        print('list is empty')
        return
      ptr = self.head
      self.head = ptr.next
      self.head.prev = None
      del(ptr)
   def deleteend(self):
    if self.head is None:
      print('list is empty')
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.prev.next = None
    del(temp)
   def deleterandom(self,pos):
    temp = self.head
    for i in range(pos):
      if temp.next is None:
        print('error')
        return
      temp = temp.next
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    del(temp)
  def search(self, ele):
    temp = self.head
    flag = -1
    if temp is None:
      print('error')
      return
    while temp :
      flag += 1
      if temp.data == ele:
        print('found', ele, 'at', flag)
        return
      temp = temp.next
      else:
        print('element not found')
  def display(self):
    temp = self.head
    print('Transversing in Forward...\n')
    while temp:
      print(temp.data, end=' ')
      last = temp
      temp = temp.next
      
    print('\nTransversing in Reverse...\n')
    while last:
      print(last.data, end=' ')
      last = last.prev
    print('\n\n')
    
l1 = DLinkedList()
print("""Operations:
0 : Stop
1 : Insert Begin
2: Insert at middle
3: Insert at end
4 : Delete Begin
5: Delete at middle
6: Delete at end
7 : Search
8: Count
9: Display""")
def main():
  ch = int(input("\n\nenter your choice: "))
  if ch == 0
  return
  elif ch == 1:
    x = int(input('enter data: '))
    l1.insert_begin(x)
    elif ch == 2:
      data1 = int(input('enter data: '))
      pos1 = int(input('enter position: '))
      l1.insert_random(data1, pos1)
   elif ch == 3:
    x = int(input('enter data: '))
    l1.insert_end(x)
   elif ch == 4:
    l1.delete_begin()
   elif ch == 5:
    pos1 = int(input('enter position: '))
    l1.delete_random(pos1)
   elif ch == 6:
    l1.delete_end()
   elif ch == 7:
    x = int(input('enter search element: '))
    l1.search(x)
   elif ch == 8:
    l1.count()
   elif ch == 9:
    l1.display()
   if ch !=0 :
    main()
main()    
   
  
  
  
  
      
      

  
   
      
 
