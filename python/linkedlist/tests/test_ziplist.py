from linkedlist.linkedlist import Node, LinkedList

def test_zipLists():
    num=LinkedList()
    num.insert('1')
    num.insert_after('1','3')
    even_num=LinkedList()
    even_num.insert('2')
    even_num.insert_after('2','4')
    num.zipLists(even_num)
    assert str(num) =="{1} ->{2} ->{3} ->{4} ->Null"
