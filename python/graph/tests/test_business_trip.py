from graph.business_trip  import  business_trip
from graph.graph  import  Graph , Vertex



def test_business_trip_1():
  g=Graph()
  v1=Vertex('Pandora')
  v2=Vertex('Arendelle')
  v3=Vertex('Metroville')
  v4=Vertex('Monstropolis')
  v5=Vertex('Narnia')
  v6=Vertex('Naboo')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,150)
  g.add_edges(v1,v3,82)
  g.add_edges(v2,v3,99)
  g.add_edges(v2,v4,42)
  g.add_edges(v3,v4,105)
  g.add_edges(v3,v5,37)
  g.add_edges(v3,v6,26)
  g.add_edges(v4,v6,73)
  g.add_edges(v6,v5,250)
  cities=["Metroville", "Pandora", ]
  actual=business_trip(g,cities)
  expected="True, $82"
  assert actual == expected



def test_business_trip_2():
  g=Graph()
  v1=Vertex('Pandora')
  v2=Vertex('Arendelle')
  v3=Vertex('Metroville')
  v4=Vertex('Monstropolis')
  v5=Vertex('Narnia')
  v6=Vertex('Naboo')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,150)
  g.add_edges(v1,v3,82)
  g.add_edges(v2,v3,99)
  g.add_edges(v2,v4,42)
  g.add_edges(v3,v4,105)
  g.add_edges(v3,v5,37)
  g.add_edges(v3,v6,26)
  g.add_edges(v4,v6,73)
  g.add_edges(v6,v5,250)
  cities=["Arendelle", "Monstropolis", "Naboo"]
  actual=business_trip(g,cities)
  expected="True, $115"
  assert actual == expected

def test_business_trip_3():
  g=Graph()
  v1=Vertex('Pandora')
  v2=Vertex('Arendelle')
  v3=Vertex('Metroville')
  v4=Vertex('Monstropolis')
  v5=Vertex('Narnia')
  v6=Vertex('Naboo')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,150)
  g.add_edges(v1,v3,82)
  g.add_edges(v2,v3,99)
  g.add_edges(v2,v4,42)
  g.add_edges(v3,v4,105)
  g.add_edges(v3,v5,37)
  g.add_edges(v3,v6,26)
  g.add_edges(v4,v6,73)
  g.add_edges(v6,v5,250)
  cities=["Naboo", "Pandora"]
  actual=business_trip(g,cities)
  expected="False, $0"
  assert actual == expected

def test_business_trip_4():
  g=Graph()
  v1=Vertex('Pandora')
  v2=Vertex('Arendelle')
  v3=Vertex('Metroville')
  v4=Vertex('Monstropolis')
  v5=Vertex('Narnia')
  v6=Vertex('Naboo')
  g.add_vertex(v1)
  g.add_vertex(v2)
  g.add_vertex(v3)
  g.add_vertex(v4)
  g.add_vertex(v5)
  g.add_vertex(v6)
  g.add_edges(v1,v2,150)
  g.add_edges(v1,v3,82)
  g.add_edges(v2,v3,99)
  g.add_edges(v2,v4,42)
  g.add_edges(v3,v4,105)
  g.add_edges(v3,v5,37)
  g.add_edges(v3,v6,26)
  g.add_edges(v4,v6,73)
  g.add_edges(v6,v5,250)
  cities=["Narnia", "Arendelle", "Naboo"]
  actual=business_trip(g,cities)
  expected="False, $0"
  assert actual == expected
