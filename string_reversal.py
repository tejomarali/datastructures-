"string reversal code"


  def __init__(self,maxs):
    self.max=maxs
    self.data=[]
    self.top=top-1
  def push(self,data):
    if self.top+1>=self.max:
      print("overflow")
    else:
      self.top=self.top+1
      self.data.insert(self.top,data)
def push(rev,x):
  rev.append(x)
  return

def pop(rev):
  if len(rev)==0:
    print("stack is empty")

  else:
    del_el=rev.pop()
  return del_el

rev_s=[]
inp=input("string:")
for a in inp:
  push(rev_s,a)
print("reversed string:")
for i in inp:
  x=pop(rev_s)
  print(x)

OUTPUT:-
string:hello
reversed string:
o
l
l
e
h
