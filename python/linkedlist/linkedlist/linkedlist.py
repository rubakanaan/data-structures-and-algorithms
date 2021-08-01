class Node:
    def __init__(self,value) :
        self.value=value
        self.next=None




class LinkedList:

    def __init__(self) :
        self.head=None

    def insert(self,value):
        node =Node(value)

        if not self.head:
            self.head=node
        else:
            node.next=self.head
            self.head=node


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


# if __name__=='__main__':
#     ruba=LinkedList()
#     ruba.insert('ruba')
#     print(ruba.to_string())

#     ruba.insert('kanaan')
#     print(ruba.to_string())
#     print(ruba.includes('ruba'))
#     print(ruba.includes('kanaan'))
#     print(ruba.includes('Hello'))






