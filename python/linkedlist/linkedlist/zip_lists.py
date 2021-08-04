from linkedlist import Node, LinkedList

def zipLists(lst, lst2):

    current = lst.head
    lst_curr = lst2.head

    while current != None and lst_curr != None:
        curr_next = current.next
        lst_next = lst_curr.next
        lst_curr.next = curr_next
        current.next = lst_curr
        current = curr_next
        lst_curr = lst_next
        lst2.head = lst_curr
    return str(lst)


if __name__=='__main__':
    ruba=LinkedList()
    ruba.insert('1')
    ruba.append('3')
    k=LinkedList()
    k.insert('2')
    k.append('4')
    k.append('5')

    if ruba.length()> k.length():

        print(zipLists(ruba,k))
    else:
        print(zipLists(k,ruba))
