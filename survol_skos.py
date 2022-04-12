import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, RDFS

g = Graph()
g.parse('https://raw.githubusercontent.com/rchateauneu/survol/master/survol/ontologies/WMI_SKOS.rdfs', format='xml')
g.namespace_manager.bind('survol', Namespace('http://www.primhillcomputers.com/survol#'), override = True)
g.serialize(destination='WMI_SKOS.ttl', format = 'turtle')