class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left=None



class BinaryTree:
  def __init__(self):
    self.pre_arr=[]
    self.in_arr=[]
    self.post_arr=[]
    self.root=None

  def pre_order(self,root):
    self.pre_arr.append(root.value)
    if root.left !=None:
      self.pre_order(root.left)
    if root.right != None:
      self.pre_order(root.right)
    return self.pre_arr


def intersection_tree(tr1,tr2):
  intersection=[]
  if tr1.root ==None or tr2.root== None:
    return None
  t1=tr1.pre_order(tr1.root)
  t2=tr2.pre_order(tr2.root)
  for element in t1:
    if element in t2:
      intersection.append(element)
  return intersection


if __name__ == "__main__":
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
  print(intersection_tree(bt,bt2))
