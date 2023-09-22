import re

from flask import jsonify, request

from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(
            f'Имя "{data["custom_id"]}" уже занято.'
        )
    if (
        len(data['custom_id']) > 16 or
        not re.compile('[0-9a-zA-Z]+$').match(data['custom_id'])
    ):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_urlmap(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if not urlmap:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urlmap.original})