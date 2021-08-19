from tree.binary_tree import Node


class Tree():
  def __init__(self) -> None:
      self.children=[]



def  fizz_buzz_tree(tree):
  new_tree=Tree()
  for node in tree.children:
    if node.value % 3 == 0 and node.value % 5 == 0:
      new_tree.children.append('FizzBuzz')
    elif node.value % 3 == 0:
      new_tree.children.append('Fizz')
    elif node.value % 5 == 0:
      new_tree.children.append('Buzz')
    else:
      new_tree.children.append(str(node.value))
  return new_tree.children





if __name__== "__main__":
  tree=Tree()
  tree.children.append(Node(18))
  tree.children.append(Node(9))
  tree.children.append(Node(1))
  tree.children.append(Node(4))
  tree.children.append(Node(13))
  print(fizz_buzz_tree(tree))
