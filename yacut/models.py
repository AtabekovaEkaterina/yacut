from datetime import datetime

from flask import url_for

from settings import MAX_LEN_FOR_ORIGINAL_LINK, MAX_LEN_FOR_SHORT_LINK
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_FOR_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_FOR_SHORT_LINK), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_view', short=self.short, _external=True)
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
