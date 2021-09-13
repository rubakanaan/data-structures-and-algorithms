# Graphs
A set of items connected by edges. Each item is called a vertex or node. Formally, a graph is a set of vertices and a binary relation between vertices, adjacency.

## Challenge

####  Features

* Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add node
  * Arguments: value
  * Returns: The added node
  * Add a node to the graph
* add edge
  * Arguments: 2 nodes to be connected by the edge, weight (optional)
  * Returns: nothing
  * Adds a new edge between two nodes in the graph
    * If specified, assign a weight to the edge
    * Both nodes should already be in the Graph
* get nodes
  * Arguments: none
  * Returns all of the nodes in the graph as a collection (set, list, or similar)
* get neighbors
  * Arguments: node
  * Returns a collection of edges connected to the given node
  * Include the weight of the connection in the returned collection
* size
  * Arguments: none
  * Returns the total number of nodes in the graph

## Breadth-First Traversal of a Graph

#### Challenge - Breadth-First-search

* Write the following method for the Graph class:
  * breadth first
  * Arguments: Node
  * Return: A collection of nodes in the order they were visited.
  * Display the collection

#### Challenge - Business-Trip

* Write a function called business trip
  * Arguments: graph, array of city names
  * Return: cost or null
* Approach & Efficiency
  * Time Complexity : O(n^2)
  * Space Complexity: O(1)
