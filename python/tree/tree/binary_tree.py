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

  def pre_order(self,root):
    self.pre_arr.append(root.value)
    if root.left !=None:
      self.pre_order(root.left)
    if root.right != None:
      self.pre_order(root.right)
    return self.pre_arr


  def in_order(self,root):

    if root.left !=None:
      self.in_order(root.left)
    self.in_arr.append(root.value)
    if root.right != None:
      self.in_order(root.right)
    return self.in_arr


  def post_order(self,root):
    if root.left !=None:
      self.post_order(root.left)
    if root.right != None:
      self.post_order(root.right)
    self.post_arr.append(root.value)
    return self.post_arr

  def find_max(self,root):
    if root is None:
      raise Exception('The Tree is empty.')
    else :
      max = root.value
      if root.left is not None:
        left = self.find_max(root.left)
        if (left > max):
            max = left
      if root.right is not None:
        right = self.find_max(root.right)
        if (right > max):
            max = right
      return max


  def __str__(self):
    ls=self.pre_order(self.root)
    tree= ''
    for i in ls:
      tree+= f"{i} "
    return tree



class BST(BinaryTree):
  def __init__(self):
    super().__init__()
    self.root=None

  def add(self,root,value):
    node=Node(value)

    if root is None:
      root = node

    else:
      if root.value == value:
        print('value = root')
      elif root.value < value:
        if root.right == None:
           root.right=node
        else:
            self.add(root.right,value)
      else:
        if root.left==None:
           root.left=node
        else:
          self.add(root.left,value)
    self.root=root




  def contains(self,root,value):

    if root is None:
      raise Exception('The Tree is empty.')
    else:
      if root.value == value:
        return True
      elif root.value < value:
        if root.right is None:
           return False
        else:
         return self.contains(root.right,value)
      else:
        if root.left is None:
           return False
        else:
         return self.contains(root.left,value)




  def __str__(self):
    ls=self.pre_order(self.root)
    tree= ''
    for i in ls:
      tree+= f"{i} "
    return tree


def breadth_first(root):

    bfs=[]
    temp=[root]
    while temp:
      curr = temp.pop(0)
      if curr.left:
        temp.append(curr.left)
      if curr.right:
        temp.append(curr.right)
      bfs.append(curr.value)
    return bfs


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)



def sum_of_odds(root):
  sum=0
  if root is None:
    raise Exception('The Tree is empty.')
  else :
    if root.value %2 == 1:
      sum+=root.value
    if root.left:
     sum+= sum_of_odds(root.left)
    if root.right:
     sum+= sum_of_odds(root.right)
  return sum




# if __name__ == "__main__":
  # bt = BinaryTree()
  # bt.root = Node(2)
  # bt.root.right = Node(5)
  # bt.root.left = Node(3)
  # bt.root.left.left = Node(15)
  # bt.root.left.right = Node(6)
  # bt.root.left.right.left = Node(5)
  # bt.root.left.right.right = Node(11)
  # bt.root.right.right = Node(9)
  # bt.root.right.right.left = Node(4)
  # print(count_nodes(bt.root))
  # print(bt)
  # print(fizz_buzz_tree(bt))
  # print(bfs)

  # print(bt.pre_order(bt.root))
  # print(bt.in_order(bt.root))
  # print(bt.post_order(bt.root))


  # b= BST()
  # b.add(b.root,5)
  # b.add(b.root,6)
  # b.add(b.root,3)
  # b.add(b.root,7)
  # b.add(b.root,2)
  # print(sum_of_odds(b.root))
  # print(b)
  # # print(b.root.right.value)

  # b= BST()
  # b.add(b.root,5)
  # b.add(b.root,7)
  # b.add(b.root,2)
  # print(b.post_order(b.root))

  # print(b.contains(b.root,7))
  # fizz_buzz_tree(bt.root)
  # print(bt)
  # bt = Tree()
