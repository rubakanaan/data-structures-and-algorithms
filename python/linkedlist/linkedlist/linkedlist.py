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


    def __str__(self):
        content=''
        current = self.head
        while current:
            content+= f"{{{str(current.value)}}} ->"
            current=current.next
        content+="Null"
        return content




if __name__=='__main__':
    ruba=LinkedList()
    ruba.insert('ruba')
    ruba.insert_after('ruba','kanaan')
    ruba.insert_after('ruba','J')
    print(str(ruba))







