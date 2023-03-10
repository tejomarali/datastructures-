"circular linked list code:"


class Node:
 def __init__(self,data):
 self.data = data
 self.link = None
class ClinkedList:
 def __init__(self):
 self.head = None
 self.tail = None
 def create(self,data):
 if self.tail is None:
 self.head = Node(data)
 self.tail = self.head
 else:
 self.tail.link = Node(data)
 self.tail = self.tail.link
 def display(self):
 cur = self.head
 if cur == None:
 print("linked list is empty")
 else:
 while cur.link != self.head:
 print(cur.data,end='->')
 cur = cur.link
 print(cur.data)
 def insertbegin(self,data):
 cur = Node(data)
 cur.link = self.head
 self.head = cur
 self.tail.link = self.head
 def insertend(self,data):
 cur = Node(data)
 self.tail.link = cur
 cur.link = self.head
 self.tail = cur
 def insertpos(self,pos,data):
 cur = Node(data)
 i = 1
 while i<pos:
 x=y
 y=y.link
 i+=1
 x.link = cur
 cur.link = y
 def deletebegin(self):
 cur = self.head
 self.head = self.head.link
 cur.link = None
 self.tail.link = self.head
 print("delete data",cur.data)
 def deleteend(self):
 cur = self.head
 while cur != self.tail:
 cur = cur.link
 cur.link = self.head
 print("deleted data",self.tail.data)
 self.tail = cur
 def deletepos(self,pos):
 cur = self.head
 i=1
 while i<pos:
 temp = cur
 cur = cur.link
 i+=1
 temp.link = cur.link
 cur.link = None
 print("deleted data",cur.data)
 def search(self,ele):
 cur = self.head
 flag = 0
 while cur is not tail:
 if ele == cur.data:
 flag = 1
 break
 cur = cur.link
 if flag == 1:
 print("element found")
 else:
 print("element not found")
 def count(self):
 cur = self.head
 c = 0
 while cur is not tail:
 cur = cur.link
 print(c)
while True:
 print(
 "1 Create \n 2 Insert in Begin \n 3 Insert in end \n 4 Insert in position \n 5 display \n 6 delete in Begin \n 7 delete in end \n 8 delete in position \n 9 Search \n 10 Count \n 11 Exit")
 ch = int(input('Enter your Choice'))
 if ch is 1:
 cll = ClinkedList()
 n = int(input('No of elements would you like to add'))
 for i in range(n):
 data = int(input('Insert data item'))
 cll.create(data)
 elif ch is 2:
 x = int(input(''))
 cll.insertbegin(x)
 elif ch == 3:
 x = int(input("Enter an element to insert at end"))
 cll.insertend(x)
 elif ch == 4:
 pos = int(input("Enter a position you want to insert the element in"))
 x = int(input("Enter an element you want to insert"))
 cll.insertpos(x, pos)
 elif ch == 5:
 cll.display()
 elif ch == 6:
 cll.deletebegin()
 elif ch == 7:
 cll.deleteend()
 elif ch == 8:
 pos = int(input("Enter the position of the element you want to delete"))
 cll.deletepos(pos)

 elif ch == 9:
 ele = int(input("Enter the element you want to search"))
 cll.search(ele)
 elif ch == 10:
 cll.count()
 elif ch == 11:
 exit() 
 
OUTPUT:-
1 Create 
 2 Insert in Begin 
 3 Insert in end 
 4 Insert in position 
 5 display 
 6 delete in Begin 
 7 delete in end 
 8 delete in position 
 9 Search 
 10 Count 
 11 Exit
Enter your Choice1
No of elements would you like to add2
Insert data item1
Insert data item2
1 Create 
 2 Insert in Begin 
 3 Insert in end 
 4 Insert in position 
 5 display 
 6 delete in Begin 
 7 delete in end 
 8 delete in position 
 9 Search 
 10 Count 
 11 Exit
Enter your Choice2
3
1 Create 
 2 Insert in Begin 
 3 Insert in end 
 4 Insert in position 
 5 display 
 6 delete in Begin 
 7 delete in end 
 8 delete in position 
 9 Search 
 10 Count 
 11 Exit
Enter your Choice7
deleted data 2
