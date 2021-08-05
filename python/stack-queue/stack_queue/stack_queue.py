class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def push(self,value):
    node=Node(value)
    node.next=self.top
    self.top=node

  def pop(self):
    current=self.top
    if self.is_empty():
      raise Exception('The stack is empty.')
    else:
      self.top=self.top.next
    return current.value


  def is_empty(self):
    return not self.top

  def peek(self):
    if self.is_empty():
      raise Exception('The stack is empty.')
    else:
      return self.top.value

  def __str__(self):
    content=''
    current = self.top
    while current:
        content+= f"{{{str(current.value)}}} ->"
        current=current.next
    content+="Null"
    return content

class Queue():
  def __init__(self):
    self.front = None
    self.rear=None

  def enqueue(self,value):
    node= Node(value)
    if self.is_empty():
      self.front=node
      self.rear=node
    else :
      node.next=self.rear
      self.rear=node


  def dequeue(self):
    temp=self.front
    if self.is_empty():
      raise Exception('The Queue is empty.')
    elif self.rear == self.front:
      self.rear=None
      self.front=None
    else:
      current=self.rear
      while current:
        if current.next==self.front:
          break
        current=current.next
      self.front=current
      current.next=None
    return temp.value


  def peek(self):
    if self.is_empty():
      raise Exception('The Queue is empty.')
    return self.front.value

  def is_empty(self):
    if (not self.rear and self.front) or (not self.front and self.rear):
      raise Exception('Somthing wrong with this Queue.')
    return not self.rear

  def __str__(self):
    content=''
    current = self.rear
    content+="Null"
    while current:
        content+= f"-> {{{str(current.value)}}}"
        current=current.next
    return content



if __name__=="__main__":
  s=Stack()
  # s.push('1')
  # print(s.peek())
  # s.push('2')
  # s.push('3')
  # print(s)
  # print(s.pop())
  # print(s.pop())
  # print(s)

  q= Queue()
  # q.enqueue('1')
  # q.enqueue('2')
  # q.enqueue('3')
  # q.enqueue('4')

  # print(q.dequeue())
  # print(q)
  # print(q.dequeue())
  # print(q)
  # print(q.dequeue())
  # print(q)
  # print(q.dequeue())
  # print(q)
  # print(q.dequeue())
  # print(q)
  # print(q.peek())
  # print(q.is_empty())
