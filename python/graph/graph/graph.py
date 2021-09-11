class Vertex:
  def __init__(self,value) -> None:
      self.value=value

class Graph:
  def __init__(self):
    self._adjacency_list = {
     # node: [edge1, edge2]
    }

  def add_vertex(self, vertex: Vertex):
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
    if vertex1 in self._adjacency_list.keys():
      if vertex2 in self._adjacency_list.keys():

        self._adjacency_list[vertex1].append([vertex2,weight])
      else:
        print('Second vertex not exist.')
    else:
        print('First vertex not exist.')


  def get_nodes(self):
    if len(list(self._adjacency_list.keys())) > 0:
      return self._breadthFirst(list(self._adjacency_list.keys())[0])
    else:
      return None

  def get_neighbors(self,vertex):
    return self._adjacency_list[vertex]


  def _breadthFirst(self,vertex):
    """
    Performs a level order traversal of the graph and calls action at each node
    """
    if vertex not in self._adjacency_list.keys():
      return None

    vertecies = []
    breadth=[vertex]
    visited = []
    visited.append(vertex)
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


  def _depthFirst(self, vertex):
    """
    Performs a depth first travesal of the graph and calls action at each node
    """
    pass

  def to_adj_list(self):
    return self._adajacency_list

if __name__=='__main__':
  g=Graph()
  g.add_vertex(Vertex('1'))
  g.add_vertex(Vertex('2'))
  g.add_vertex(Vertex('3'))
  g.add_vertex(Vertex('4'))
  g.add_edges('1','2',4)
  g.add_edges('1','3',9)
  g.add_edges('1','4',3)
  g.add_edges('2','1',4)
  g.add_edges('3','1',3)
  g.add_edges('3','4',6)
  g.add_edges('4','1',9)
  g.add_edges('4','2',5)
  g.add_edges('4','3',6)
  # print(g._breadthFirst('1'))
  # print (g.get_nodes())
  print(g.get_neighbors('1'))
  # print(g.size())

