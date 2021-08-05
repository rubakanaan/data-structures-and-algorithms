from stack_queue.stack_queue import Stack,Queue,Node
import pytest


def test_push():
  s=Stack()
  s.push('1')
  assert str(s)== "{1} ->Null"

def  test_push_multiple():
  s=Stack()
  s.push('1')
  s.push('2')
  s.push('3')
  assert str(s)== "{3} ->{2} ->{1} ->Null"

def test_pop():
  s=Stack()
  s.push('1')
  s.push('2')
  s.pop()
  assert str(s)=="{1} ->Null"


def test_multiple_pop():
  s=Stack()
  s.push('1')
  s.push('2')
  s.pop()
  s.pop()
  assert s.is_empty()

def test_peek_stack():
  s=Stack()
  s.push('1')
  assert s.peek() == '1'

def test_is_empty_stack():
  s=Stack()
  assert s.is_empty()


def test_peek_when_empty_stack():
  s=Stack()
  with pytest.raises(Exception, match='The stack is empty.'):
    s.peek()

##############################################################################################################

def test_enqueue():
  q=Queue()
  q.enqueue('1')
  assert str(q)=="Null-> {1}"

def test_multiple_enqueue():
  q=Queue()
  q.enqueue('1')
  q.enqueue('2')
  assert str(q)== "Null-> {2}-> {1}"


def test_dequeue():
  q=Queue()
  q.enqueue('1')
  q.enqueue('2')
  assert q.dequeue() == '1'

def test_peek_queue():
  q=Queue()
  q.enqueue('1')
  q.enqueue('2')
  assert q.peek() == '1'

def test_multiple_dequeue():
  q=Queue()
  q.enqueue('1')
  q.enqueue('2')
  q.dequeue()
  q.dequeue()
  assert q.is_empty()

def test_is_empty_queue():
  q=Queue()
  assert q.is_empty()

def test_peek_when_empty_queue():
  q=Queue()
  with pytest.raises(Exception, match='The Queue is empty.'):
    q.peek()

