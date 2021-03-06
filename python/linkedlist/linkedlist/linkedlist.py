from typing import Counter
from checklist import isPalindrome

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def append(self, value):
      current = self.head
      node = Node(value)
      while current:
          if current.next == None:
              current.next = node
              node.next = None
          current = current.next

    def insert_after(self, value, new_value):
        current = self.head
        node = Node(new_value)
        while current:
            if current.value == value:
              node.next = current.next
              current.next = node
            current= current.next

    def insert_before(self, value, new_value):
        if self.head.value==value:
            self.insert(new_value)
        else:
            current = self.head
            node = Node(new_value)
            while current.next:
                if  current.next.value == value:
                    node.next=current.next
                    current.next=node
                    break
                current= current.next


    def includes(self,value):
        current=self.head
        while current:
           if current.value == value:
               return True
           current=current.next
        return False

    def kth_from_end(self, k):
        current = self.head
        counter = -1
        while current is not None:
            current = current.next
            counter += 1

        if k > counter:
            return ('K is out of range')
        if k < 0:
            return 'K is a negative number'
        current = self.head
        for i in range(0, counter - k):
            current = current.next
        return int(current.value)


    def length(self):
        counter=0
        current=self.head
        while current:

               counter+=1
               current=current.next
        return counter

    def __str__(self):
        content=''
        current = self.head
        while current:
            content+= f"{{{str(current.value)}}} ->"
            current=current.next
        content+="Null"
        return content



if __name__=='__main__':
    # ruba=LinkedList()
    # ruba.insert('1')
    # ruba.append('3')
    # k=LinkedList()
    # k.insert('2')
    # k.append('4')
    # k.append('5')

    lnl=LinkedList()
    lnl.insert('h')
    lnl.append('i')
    lnl.append('hi')
    lnl.append('m')
    print(str(lnl))







