from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class searchForm(Form):
	keyword = StringField('keyword')
	filters = SelectField('filters', choices=[('po', 'Plant Ontology'),
											   ('go', 'Gen Ontology')])