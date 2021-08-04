# Singly Linked List

- a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using
references
- Singly linked list means that there is only one reference, and the reference points to the Next node in a linked list.

## Challenge:

### Features

### Node
* Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Linked List
* Create a Linked List class
* Within your Linked List class, include a head property.
    * Upon instantiation, an empty Linked List should be created.
    * The class should contain the following methods
* insert
    * Arguments: value
    * Returns: nothing
    * Adds a new node with that value to the head of the list with an O(1) Time performance.
* includes
    * Arguments: value
    * Returns: Boolean
    * Indicates whether that value exists as a Node’s value somewhere within the list.
* to string
    * Arguments: none
    * Returns: a string representing all the values in the Linked List, formatted as:
 "{ a } -> { b } -> { c } -> NULL"

* append
  * arguments: new value
  * adds a new node with the given value to the end of the list
* insert before
  * arguments: value, new value
  * adds a new node with the given new value immediately before the first node that has the value specified
* insert after
  * arguments: value, new value
  * adds a new node with the given new value immediately after the first node that has the value specified


* kth from end
  * argument: a number, k, as a parameter.
  * Return the node’s value that is k places from the tail of the linked list.
  * You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.



* zipLists
  * Write a function called zip lists
  * Arguments: 2 linked lists
  * Return: Linked List, zipped with each others
  * Zip the two linked lists together into one so that the nodes alternate between the two lists and return a          reference to the head of the zipped list.
  * Try and keep additional space down to O(1)
  * You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
