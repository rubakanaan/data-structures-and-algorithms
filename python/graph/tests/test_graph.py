from graph import __version__
from graph.graph  import  Graph , Vertex

def test_version():
    assert __version__ == '0.1.0'


def test_add_vertex():
  g=Graph()
  g.add_vertex(Vertex("1"))


def test_add_edge():
  g=Graph()
  g.add_vertex(Vertex("1"))
  g.add_vertex(Vertex("2"))


def test_get_nodes():
  g=Graph()
  v1=Vertex('1')
  v2=Vertex('2')
  v3=Vertex('3')
  v4=Vertex('4')
  v5=Vertex('5')
  v6=Vertex('6')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,4)
  g.add_edges(v2,v3,9)
  g.add_edges(v2,v4,3)
  g.add_edges(v3,v4,4)
  g.add_edges(v3,v4,3)
  g.add_edges(v3,v5,6)
  g.add_edges(v4,v6,9)
  g.add_edges(v6,v5,5)
  assert g.get_nodes()== ["1","2","3","4","5","6"]


def test_get_neighbors():
  g=Graph()
  v1=Vertex('1')
  v2=Vertex('2')
  v3=Vertex('3')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_edges(v1,v2,4)
  g.add_edges(v2,v3,9)
  actual=g.get_neighbors("1")
  expected= [['2', 4]]
  assert actual== expected


def test_get_size():
  g=Graph()
  g.add_vertex(Vertex('1'))
  g.add_vertex(Vertex('2'))
  g.add_vertex(Vertex('3'))
  g.add_vertex(Vertex('4'))
  actual = g.size()
  expected= 4
  assert actual==expected

def test_empty_graph():
  g=Graph()
  assert g.get_nodes() == None


def test_breadth_first():
  g=Graph()
  v1=Vertex('Pandora')
  v2=Vertex('Arendelle')
  v3=Vertex('Metroville')
  v4=Vertex('Monstroplolis')
  v5=Vertex('Narnia')
  v6=Vertex('Naboo')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,4)
  g.add_edges(v2,v3,9)
  g.add_edges(v2,v4,3)
  g.add_edges(v3,v4,4)
  g.add_edges(v3,v4,3)
  g.add_edges(v3,v5,6)
  g.add_edges(v4,v6,9)
  g.add_edges(v6,v5,5)
  actual = g.breadthFirst(v1)
  expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
  assert actual == expected



def test_breadthFirst():
  g=Graph()
  v1=Vertex('Pandora')
  actual = g.breadthFirst(v1)
  expected= None
  assert actual==expected
