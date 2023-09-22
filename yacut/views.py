from random import choice
import string

from flask import abort, flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap


def get_unique_short_id():
    random_symbol = string.ascii_letters + string.digits
    while True:
        short = ''.join(choice(random_symbol) for _ in range(6))
        if not URLMap.query.filter_by(short=short).first():
            break
    return short


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        if form.custom_id.data:
            if URLMap.query.filter_by(short=form.custom_id.data).first():
                flash(f'Имя {form.custom_id.data} уже занято!', 'error-message')
                return render_template('index.html', form=form)
            short = form.custom_id.data
        else:
            short = get_unique_short_id()
        urlmap = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(url_for('redirect_view', short=short, _external=True), 'short-message')
    return render_template('index.html', form=form)


@app.route('/<path:short>')
def redirect_view(short):
    urlmap = URLMap.query.filter_by(short=short).first()
    if urlmap:
        return redirect(urlmap.original)
    abort(404)
