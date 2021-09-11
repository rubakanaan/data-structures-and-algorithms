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
  assert g.get_nodes()== ["1","2","3","4"]


def test_get_neighbors():
  g=Graph()
  g.add_vertex(Vertex('1'))
  g.add_vertex(Vertex('2'))
  g.add_vertex(Vertex('3'))
  g.add_vertex(Vertex('4'))
  g.add_edges('1','2',4)
  g.add_edges('1','3',9)
  g.add_edges('1','4',3)
  actual=g.get_neighbors("1")
  expected= [['2', 4], ['3', 9], ['4', 3]]
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

def test_one_vertex():
  g=Graph()
  g.add_vertex(Vertex('1'))
  g.add_edges('1','1',9)
  assert g.get_nodes() == ["1"]
  assert g.get_neighbors("1")== [['1',9]]

def test_empty_graph():
  g=Graph()
  assert g.get_nodes() == None
