from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired
from mash_place_ui.models import Constituency, County
import json

constituency = Constituency()
constituencies = json.loads(constituency.get_constituencies())

CONSTITUENCIES = []

for item in constituencies:
    CONSTITUENCIES.append((item['ons_code'], item['name']))

county = County()
counties = json.loads(county.get_counties())

COUNTIES = []

for item in counties:
    COUNTIES.append((item['ons_code'], item['name']))


class ConstituencyForm(Form):
    constituency = SelectField('Constituency', choices=CONSTITUENCIES, validators=[DataRequired()])


class CountyForm(Form):
    county = SelectField('County', choices=COUNTIES, validators=[DataRequired()])
