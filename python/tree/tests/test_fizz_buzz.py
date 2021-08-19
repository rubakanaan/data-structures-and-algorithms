from tree.k_arry_tree import Tree,fizz_buzz_tree
from tree.binary_tree import Node



def test_fizz_buzz():
  tree=Tree()
  tree.children.append(Node(18))
  tree.children.append(Node(5))
  tree.children.append(Node(1))
  tree.children.append(Node(4))
  tree.children.append(Node(15))
  assert fizz_buzz_tree(tree) == ['Fizz', 'Buzz', '1', '4', 'FizzBuzz']

def test_fizz_buzz_empty():
  tree=Tree()
  assert fizz_buzz_tree(tree) == []

