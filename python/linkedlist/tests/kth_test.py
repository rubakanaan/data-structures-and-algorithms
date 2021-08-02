from linkedlist.linkedlist import Node, LinkedList

def test_kth_from_end():
  ruba = LinkedList()
  ruba.insert('1')
  ruba.insert_after('1','2')
  assert ruba.kth_from_end(0)==2

def test_kth_from_end_greater():
  ruba = LinkedList()
  ruba.insert('1')
  ruba.insert_after('1','2')
  assert ruba.kth_from_end(3)== "K is out of range"

def test_kth_from_end_same_len():
  ruba = LinkedList()
  ruba.insert('1')
  ruba.insert_after('1','2')
  assert ruba.kth_from_end(1)==1

def test_kth_from_end_negative():
  ruba = LinkedList()
  ruba.insert('1')
  ruba.insert_after('1','2')
  assert ruba.kth_from_end(-1)== 'K is a negative number'
