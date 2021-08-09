from stack_queue.stack_queue import Node

class AnimalShelter:
  def __init__(self):
    self.front = None
    self.rear=None



  def enqueue(self,animal):
    animal= Node(animal)
    if  self.is_empty():
      self.front=animal
      self.rear=animal
    else :
      self.rear.next=animal
      self.rear=animal



  def dequeue (self,pref):
    if pref == "dog" or pref.lower() == "cat":
      if self.is_empty():
        raise Exception('The Shelter is empty.')
      else:
        if pref == self.front.value:
          temp=self.front
          self.front=self.front.next
          return temp.value
        else:
          current=self.front
          while current.next:
            if current.next.value == pref:
              temp=current.next
              current.next=current.next.next
            else:
              current=current.next
          return temp.value
    else:
      return "null"


  def is_empty(self):
    if self.front:
      return False
    else:
      return True

  def __str__(self):
    content=''
    current = self.front
    while current:
        content+= f"{{{str(current.value)}}}<-"
        current=current.next
    content+="Null"
    return content









# if __name__=="__main__":
#   animal=AnimalShelter()
#   # animal.enqueue('cat')
#   animal.enqueue('cat')
#   animal.enqueue('dog')
#   print(animal.dequeue('dog'))
#   print(animal)
