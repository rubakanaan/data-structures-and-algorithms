import pytest
from linkedlist.linkedlist import Node, LinkedList


def test_linked_test():
    # with pytest.raises(ImportError):
    #      'ImportError'
    assert LinkedList()


def test_insert():
    ruba = LinkedList()
    ruba.insert('ruba')
    assert ruba.includes('ruba')


def test_head():
    # with pytest.raises(AttributeError):
    #      raise Exception('AttributeError')
    ruba = LinkedList()
    ruba.insert('ruba')
    assert ruba.head.value


def test_multiple_insert():
    ruba = LinkedList()
    ruba.insert('ruba')
    ruba.insert('kanaan')
    assert str(ruba)== '{kanaan} ->{ruba} ->Null'


def test_includes():
    ruba = LinkedList()
    ruba.insert('ruba')
    assert ruba.includes('ruba')


def test_not_includes():
    ruba = LinkedList()
    assert ruba.includes('ruba') == False


def test_to_string():
    ruba = LinkedList()
    ruba.insert('ruba')
    ruba.insert('kanaan')
    assert str(ruba) == '{kanaan} ->{ruba} ->Null'

def test_append():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.append('kanaan')
  assert str(ruba) == '{ruba} ->{kanaan} ->Null'

def test_multiple_append():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.append('J')
  ruba.append('kanaan')
  assert str(ruba) == '{ruba} ->{J} ->{kanaan} ->Null'

def test_insert_before():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.append('kanaan')
  ruba.insert_before('kanaan','J')
  assert str(ruba)== '{ruba} ->{J} ->{kanaan} ->Null'

def test_insert_before_first():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.insert_before('ruba','I\'m')
  assert str(ruba)== '{I\'m} ->{ruba} ->Null'

def test_inser_after():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.append('kanaan')
  ruba.insert_after('ruba','J')
  assert str(ruba)== "{ruba} ->{J} ->{kanaan} ->Null"

def test_inser_after_last():
  ruba = LinkedList()
  ruba.insert('ruba')
  ruba.insert_after('ruba','kanaan')
  assert str(ruba)== '{ruba} ->{kanaan} ->Null'








