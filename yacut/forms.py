from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import (MAX_LEN_FOR_ORIGINAL_LINK,
                      MAX_LEN_FOR_SHORT_LINK,
                      VALID_NAME_FOR_SHORT_LINK)


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(max=MAX_LEN_FOR_ORIGINAL_LINK)]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[Regexp(VALID_NAME_FOR_SHORT_LINK, message='Недопустимое имя'),
                    Length(max=MAX_LEN_FOR_SHORT_LINK),
                    Optional()]
    )
    submit = SubmitField('Создать')