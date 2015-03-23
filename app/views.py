from flask import render_template, flash, redirect, request, url_for
from app import app
from rdflib import Graph
from .forms import searchForm

@app.route('/')
@app.route('/index')
def index():
	form = searchForm()
	return render_template('index.html',title='Home',form=form)

@app.route('/search/',methods=['GET','POST'])
def search():
	keyword = request.form['keyword']
	filters = request.form['filters']

	if filters == 'po':
		poGraph = Graph().parse("ontology.owl")
		qres = poGraph.query( 
			""" PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
				PREFIX owl: <http://www.w3.org/2002/07/owl#>
				PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
				PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
				PREFIX obo: <http://purl.obolibrary.org/obo/>
				PREFIX po: <http://purl.obolibrary.org/po#>

				SELECT ?label ?comment
				WHERE
				{ ?s rdfs:label ?label ; 
		  		  	 rdfs:comment ?comment .
		  		  	 FILTER (REGEX(?label,""" '"'+ request.form['keyword'] +'"' ""","i")
		  		  			|| REGEX(?comment,""" '"'+ request.form['keyword'] +'"' ""","i"))
		  		 }"""
			)
		# qres = "Test Result"
	else:
		goGraph = Graph().parse("go.owl")
		qres = goGraph.query( 
			""" PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
				PREFIX owl: <http://www.w3.org/2002/07/owl#>
				PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
				PREFIX oboInOwl: <http://www.geneontology.org/formats/oboInOwl#>
				PREFIX obo: <http://purl.obolibrary.org/obo/>
				PREFIX po: <http://purl.obolibrary.org/po#>

				SELECT ?label ?comment
				WHERE
				{ ?s rdfs:label ?label ; 
		  				 		 rdfs:comment ?comment .
		  				 		 }"""
			)
	# if qres.row == 0: qres = 'Not Found'
	return render_template('result.html',keyword=keyword,filters=filters,qres=qres)