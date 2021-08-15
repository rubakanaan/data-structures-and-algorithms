from tree.binary_tree import Node, BinaryTree, BST



def test_add_bst():
  b= BST()
  b.add(b.root,5)
  assert b.root.value == 5

def test_add_bst_left():
  b= BST()
  b.add(b.root,5)
  b.add(b.root,2)
  assert b.root.left.value == 2

def test_add_bst_right():
  b= BST()
  b.add(b.root,5)
  b.add(b.root,7)
  assert b.root.right.value == 7

def test_pre_order():
  b= BST()
  b.add(b.root,5)
  b.add(b.root,7)
  b.add(b.root,2)
  assert b.pre_order(b.root)== [5, 2, 7]

def test_in_order():
  b= BST()
  b.add(b.root,5)
  b.add(b.root,7)
  b.add(b.root,2)
  assert b.in_order(b.root)== [2, 5, 7]

def test_post_order():
  b= BST()
  b.add(b.root,5)
  b.add(b.root,7)
  b.add(b.root,2)
  assert b.post_order(b.root)== [2, 7, 5]


def test_find_max():
  bt = BinaryTree()
  bt.root = Node(2)
  bt.root.right = Node(5)
  bt.root.left = Node(7)
  bt.root.left.left = Node(2)
  bt.root.left.right = Node(9)
  bt.root.left.right.left = Node(5)
  assert bt.find_max(bt.root) == 9
