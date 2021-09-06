from hash_table.intersection_tree import Node , BinaryTree, intersection_tree


def test_intersection_tree():
  bt = BinaryTree()
  bt.root = Node(2)
  bt.root.right = Node(5)
  bt.root.left = Node(3)
  bt.root.left.left = Node(15)
  bt.root.left.right = Node(6)
  bt.root.left.right.left = Node(1)
  bt2 = BinaryTree()
  bt2.root = Node(5)
  bt2.root.right = Node(1)
  bt2.root.left = Node(3)
  bt2.root.left.left = Node(15)
  bt2.root.left.right = Node(7)
  bt2.root.left.right.left = Node(9)
  expected=[3, 15, 1, 5]
  actual= intersection_tree(bt,bt2)
  assert expected==actual

def test_one_empty_tree():
  bt = BinaryTree()
  bt.root = Node(2)
  bt.root.right = Node(5)
  bt.root.left = Node(3)
  bt.root.left.left = Node(15)
  bt.root.left.right = Node(6)
  bt.root.left.right.left = Node(1)
  bt2 = BinaryTree()
  expected=None
  actual= intersection_tree(bt,bt2)
  assert expected==actual

def test_both_empty_trees():
  bt = BinaryTree()
  bt2 = BinaryTree()
  expected=None
  actual= intersection_tree(bt,bt2)
  assert expected==actual
