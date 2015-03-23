from rdflib import Graph

g = Graph().parse("go.owl")
# g.parse("http://purl.obolibrary.org/obo/PO_0009011")
qres = g.query( 
	""" PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
		PREFIX owl: <http://www.w3.org/2002/07/owl#>
		PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
		PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
		PREFIX obo: <http://purl.obolibrary.org/obo/>
		PREFIX po: <http://purl.obolibrary.org/po#>

		SELECT DISTINCT ?p
		WHERE
		{ ?s ?p ?o .
		  				 }"""
	)
for row in qres:
	print(" %s " % row)

# import pprint
# for stmt in g:
# 	pprint.pprint(stmt)	