class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node


class HashTable:

  def __init__(self,size=1024) -> None:
      self.bucket=[None]* size
      self.size= size

  def add(self,key,value):
    """
    This method should take the key and value pair and add it to the table
    Arguments: key, value
    Returns: nothing

    """

    index = self.hash(key)

    if self.bucket[index]== None:
      self.bucket[index]=LinkedList()
    self.bucket[index].insert([key,value])




  def get(self,key):
    """
    This method should take a key and return the value assosiated with that key.
    Arguments: key
    Returns: Value
    """

    index = self.hash(key)
    if self.bucket[index]== None:
      return None
    else:
      current = self.bucket[index].head
      while current:
        if current.value[0] == key:
            return current.value[1]
        current = current.next



  def contains(self,key):
    """
    This method takes a key and check if its in the table.
    Arguments: key
    Returns: Boolean
    """

    index = self.hash(key)
    if self.bucket[index] == None:
      return False
    else:
      current = self.bucket[index].head
      while current:
        if current.value[0] == key:
            return True
        else:
          return False



  def hash(self,key):
    """
    This method take a key as string and return the index of where this key should be in the hash table.
    Arguments: key
    Returns: Index
    """
    value= 0
    for letter in key:
      value+= ord(letter)
    index = value * 5 % self.size
    return index


if __name__ == "__main__":
  hash=HashTable()
  hash.add('1','Ruba')
  hash.add('2', 'Kanaan')
  print(hash.get('1'))
  print(hash.get('2'))
  print(hash.get('22'))
  print(hash.contains('16'))
  print(hash.contains('1'))
  for i in hash.bucket:
    if i != None:
      print ( i.head.value[0])
