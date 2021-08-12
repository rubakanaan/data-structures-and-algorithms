# Trees

Common Terminology Node - A node is the individual item/data that make up the data structure Root - The root is the first/top Node in the tree Left Child - The node that is positioned to the left of a root or node Right Child - The node that is positioned to the right of a root or node Edge - The edge in a tree is the link between a parent and child node Leaf - A leaf is a node that does not contain any children Height - The height of a tree is determined by the number of edges from the root to the bottommost node
## PR:
* https://github.com/rubakanaan/data-structures-and-algorithms/pull/29

## Features

* Node
  *Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
* Binary Tree
  * Create a Binary Tree class
  * Define a method for each of the depth first traversals:
    * pre order
    * in order
    * post order which returns an array of the values, ordered appropriately.

* Binary Search Tree
  * Create a Binary Search Tree class
  * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  * Add
    * Arguments: value
    * Return: nothing
    * Adds a new node with that value in the correct location in the binary search tree.
  * Contains
    * Argument: value
    * Returns: boolean indicating whether or not the value is in the tree at least once.

