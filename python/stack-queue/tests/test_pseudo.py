from stack_queue.pseudo import PseudoQueue
from stack_queue.stack_queue import Stack


def test_enqueue():
  p=PseudoQueue()
  p.enqueue('1')
  assert str(p)=="Null-> {1}"


def test_dequeue():
  p=PseudoQueue()
  p.enqueue('1')
  p.enqueue('2')
  assert str(p.dequeue()) == '1'
