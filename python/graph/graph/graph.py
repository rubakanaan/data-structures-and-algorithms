class Vertex:
  def __init__(self,value) -> None:
      self.value=value

class Edge:

  def __init__(self, vertex, weight=1):
    self.vertex=vertex
    self.weight=weight

class Graph:
  def __init__(self):
    self._adjacency_list = {
    }

  def add_vertex(self, vertex):
    """
    Adds a vertex to the graph

    arguments
    vertex: Vertex
    """
    self._adjacency_list[vertex.value]=[]

  def add_edges(self, vertex1, vertex2, weight=1):
    """
    Adds an edge to our graph

    """
    if vertex1.value in self._adjacency_list.keys():
      if vertex2.value in self._adjacency_list.keys():
        edge=Edge(vertex2,weight)
        self._adjacency_list[vertex1.value].append([edge.vertex.value , edge.weight])
        edge=Edge(vertex1,weight)
        self._adjacency_list[vertex2.value].append([edge.vertex.value , edge.weight])
      else:
        print('Second vertex not exist.')
    else:
        print('First vertex not exist.')


  def get_nodes(self):
    if len(list(self._adjacency_list.keys())) > 0:
       return list(self._adjacency_list)
    else:
      return None

  def get_neighbors(self,vertex):
    return self._adjacency_list[vertex]


  def breadthFirst(self,vertex):
    """
    Performs a level order traversal of the graph and calls action at each node
    """
    if vertex.value not in self._adjacency_list.keys():
      return None

    vertecies = []
    breadth=[vertex.value]
    visited = []
    visited.append(vertex.value)
    while len(breadth)!= 0:
      front= breadth.pop(0)
      vertecies.append(front)
      for i in self._adjacency_list[front]:
        if i[0] not in visited :
          visited.append(i[0])
          breadth.append(i[0])
    return vertecies

  def size(self):
    return len(self._adjacency_list)


  def depthFirst(self, vertex):
    """
    Performs a depth first travesal of the graph and calls action at each node
    """
    if vertex.value not in self._adjacency_list.keys():
      return None

    vertecies = []
    depth=[vertex.value]
    visited = [vertex.value]
    while len(depth)!= 0:
      last= depth.pop()
      vertecies.append(last)
      for i in self._adjacency_list[last]:
        if i[0] not in visited :
          visited.append(i[0])
          depth.append(i[0])
    return vertecies


  def to_adj_list(self):
    return self._adajacency_list




if __name__=='__main__':
  g=Graph()
  v1=Vertex('a')
  v2=Vertex('b')
  v3=Vertex('d')
  v4=Vertex('f')
  v5=Vertex('h')
  v6=Vertex('e')
  v7=Vertex('c')
  v8=Vertex('g')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_vertex(v7)
  g.add_vertex(v8)
  g.add_edges(v1,v3,4)
  g.add_edges(v1,v2,9)
  g.add_edges(v2,v3,3)
  g.add_edges(v2,v7,4)
  g.add_edges(v3,v4,3)
  g.add_edges(v3,v5,6)
  g.add_edges(v3,v6,6)
  g.add_edges(v4,v5,9)
  g.add_edges(v7,v8,5)

  print(g.depthFirst(v1))
  # print (g.get_nodes())
  # print(g.get_neighbors(v1))
  # print(g.size())
  # print(g._adjacency_list)

