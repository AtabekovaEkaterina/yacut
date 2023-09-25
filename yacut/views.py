from flask import flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLMapForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


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
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(urlmap.original)
