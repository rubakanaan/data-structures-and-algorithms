from graph.graph  import  Graph , Vertex



def test_depth_first():
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
  actual=g.depthFirst(v1)
  expected=['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
  assert actual == expected

def test_depth_first_not_found():
  g=Graph()
  v1=Vertex('k')
  actual = g.breadthFirst(v1)
  expected= None
  assert actual==expected
