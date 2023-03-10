'''single linked list:
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
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def insertSLL(self, value, location):
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if location == 0:
                    newNode.next = self.head
                    self.head = newNode
                elif location == -1:
                    newNode.next = None
                    self.tail.next = newNode
                    self.tail = newNode
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                    if tempNode == self.tail:
                        self.tail = newNode
    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # to count the number of nodes in the linked list
    def countnodesSLL(self):
        count = 0
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                node = node.next
                count += 1
        return count

    # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

    #  Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


# this will show the linked list with the elements included
singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
print(singlyLinkedList.traverseSLL())
singlyLinkedList.insertSLL(2, 1)
print(singlyLinkedList.traverseSLL())
singlyLinkedList.insertSLL(3, 1)
print(singlyLinkedList.traverseSLL())
singlyLinkedList.insertSLL(4, 1)
print(singlyLinkedList.traverseSLL())
singlyLinkedList.insertSLL(5, -1)
print(singlyLinkedList.traverseSLL())
singlyLinkedList.insertSLL(15, 3)
print(singlyLinkedList.traverseSLL())
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.countnodesSLL())
singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList])
print(SLinkedList)

