from graph.graph import Graph , Vertex

def business_trip(graph, cities):
  flag=False
  cost=0
  for i in range(len(cities)):
    neighbor=graph.get_neighbors(cities[i])
    for k in range(len(neighbor)):
      if i+1 < len(cities):
        if cities[i+1] == neighbor[k][0]:
          flag= True
          cost+=neighbor[k][1]
  return f"{flag}, ${cost}"



if __name__=='__main__':
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
  print(business_trip(g,cities))

