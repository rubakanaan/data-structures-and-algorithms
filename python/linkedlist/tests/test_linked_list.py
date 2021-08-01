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






