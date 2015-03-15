from flask import render_template
from app import app
from rdflib import Graph

@app.route('/')
@app.route('/index')
def index():
	g = Graph().parse("ontology.owl")
	qres = g.query( 
	""" PREFIX rdfs: < #>
		PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
		PREFIX owl: <http://www.w3.org/2002/07/owl#>
		PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
		PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
		PREFIX obo: <http://purl.obolibrary.org/obo/>
		PREFIX po: <http://purl.obolibrary.org/po#>

		SELECT DISTINCT ?label ?comment
		WHERE
		{ obo:PO_0009011 rdfs:label ?label ; 
		  				 rdfs:comment ?comment .
		  				 }"""
	)
	# for row in qres:
	# 	term = "%s" 
	# 	definition = "%s" % row
	return render_template('index.html',title='Home',query=qres)

