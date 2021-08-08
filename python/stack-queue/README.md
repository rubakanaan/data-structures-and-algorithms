# Stacks and Queues

* **Stack** : A collection of items in which only the most recently added item may be removed. The latest added item is at the top. Basic operations are push and pop.
* **Queue**:   A collection of items in which only the earliest added item may be accessed. Basic operations are add (to the tail) or enqueue and delete (from the head) or dequeue.

## PR:

* https://github.com/rubakanaan/data-structures-and-algorithms/pull/24

## Challenge

### Node

  * Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

### Stack

  * Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  * This object should be aware of a default empty value assigned to top when the stack is created.

**The class should contain the following methods:**
* push
  * Arguments: value
  * adds a new node with that value to the top of the stack with an O(1) Time performance.
* pop
  * Arguments: none
  * Returns: the value from node from the top of the stack
  * Removes the node from the top of the stack
  * Should raise exception when called on empty stack
* peek
  * Arguments: none
  * Returns: Value of the node located at the top of the stack
  * Should raise exception when called on empty stack
* is empty
  * Arguments: none
  * Returns: Boolean indicating whether or not the stack is empty.


### Queue

* Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  * This object should be aware of a default empty value assigned to front when the queue is created.
**The class should contain the following methods:**

* enqueue
  * Arguments: value
  * adds a new node with that value to the back of the queue with an O(1) Time performance.
* dequeue
  * Arguments: none
  * Returns: the value from node from the front of the queue
  * Removes the node from the front of the queue
  * Should raise exception when called on empty queue
* peek
  * Arguments: none
  * Returns: Value of the node located at the front of the queue
  * Should raise exception when called on empty stack
*is empty
  * Arguments: none
  * Returns: Boolean indicating whether or not the queue is empty


## PseudoQueue

* Create a new class called pseudo queue.
  * Do not use an existing Queue.
  * Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
  * Internally, utilize 2 Stack instances to create and manage the queue
* Methods:
  * enqueue
    * Arguments: value
    * Inserts value into the PseudoQueue, using a first-in, first-out approach.
  * dequeue
  * Arguments: none
  * Extracts a value from the PseudoQueue, using a first-in, first-out approach.
