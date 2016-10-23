from mash_place import app, cache
from flask import render_template
from mash_place.models import Constituency
from mash_place.forms import Search
import json

constituency = Constituency()


@app.route('/boundaries/constituencies', methods=["GET", "POST"])
def constituencies():
    form = Search()
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
