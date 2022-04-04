import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, RDFS

g = Graph()
g.parse('https://raw.githubusercontent.com/rchateauneu/survol/master/survol/ontologies/WMI_RDFS.rdfs', format='xml')
g.namespace_manager.bind('survol', Namespace('http://www.primhillcomputers.com/survol#'), override = True)

print('Parsing done.')

df = rdfpandas.to_dataframe(g)

print('Transform done.')

# As of this writing WMI_RDFS.rdfs does not have rdfs:subClassOf and rdfs:subPropertyOf statements
clean_df = df[['rdf:type{URIRef}', 'rdfs:comment{Literal}', 'rdfs:label{Literal}']]

print('Selection done.')

clean_df.to_csv('survol.csv', index = True, index_label = '@id', encoding='utf-8-sig')

print('Writing done.')
