from flask_wtf import Form
from wtforms import SelectField
from wtforms.validators import DataRequired
from mash_place.models import Constituency
import json

constituency = Constituency()
constituencies = json.loads(constituency.get_constituencies())

CONSTITUENCIES = []

for item in constituencies:
    CONSTITUENCIES.append((item['ons_code'], item['name']))


class Search(Form):
    constituency = SelectField('Constituency', choices=CONSTITUENCIES, validators=[DataRequired()])
