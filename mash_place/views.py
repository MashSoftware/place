from mash_place import app, cache
from flask import render_template
from mash_place.models import Constituency, County
from mash_place.forms import ConstituencyForm, CountyForm
import json

constituency = Constituency()
county = County()


@app.route('/boundaries/constituencies', methods=["GET", "POST"])
def constituencies():
    form = ConstituencyForm()
    if form.validate_on_submit():
        data = json.loads(constituency.get_constituency(form.constituency.data))

        return render_template(
            'constituencies.html',
            data=data,
            form=form
        )

    return render_template(
        'constituencies.html',
        form=form
    )


@app.route('/boundaries/counties', methods=["GET", "POST"])
def counties():
    form = CountyForm()
    if form.validate_on_submit():
        data = json.loads(county.get_county(form.county.data))

        return render_template(
            'counties.html',
            data=data,
            form=form
        )

    return render_template(
        'counties.html',
        form=form
    )


@app.route('/about', methods=["GET"])
@cache.cached(timeout=3600)
def about():
    return render_template(
        'about.html'
    )


@app.errorhandler(400)
def bad_request(error):
    return render_template('error.html', error=error), 400


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error=error), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error), 500
