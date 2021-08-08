from stack_queue.stack_queue import Stack

class PseudoQueue:
  def __init__(self) -> None:
    self.top=None


  def enqueue(self,value):
    Stack.push(self,value)

  def dequeue(self):
    current=self.top
    temp=Stack()
    while current :
      temp.push(current.value)
      Stack.pop(self)
      current=current.next

    output=temp.pop()
    current=temp.top

    while current :
      Stack.push(self,current.value)
      current=current.next
    return output





  def is_empty(self):
    return not self.top


  def __str__(self):
      content=''
      current = self.top
      content+="Null"
      while current:
          content+= f"-> {{{str(current.value)}}}"
          current=current.next
      return content


if __name__=="__main__":
  p=PseudoQueue()
  p.enqueue('1')
  p.enqueue('2')
  p.enqueue('3')
  p.dequeue()
  p.dequeue()
  print(p)
