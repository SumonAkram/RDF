from rdflib import Graph, Namespace, RDF

# Defining namespaces
ex = Namespace("http://example.org/")

# Creating RDF graph
g = Graph()

# Parsing the RDF Turtle data
g.parse("rdf_data.ttl", format="turtle") #path, format

# Iterating through triples
for s, p, o in g:
    print(s, p, o) 