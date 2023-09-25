from random import choice
import string

from settings import NUMBER_OF_CHARACTERS_TO_GENERATE_SHORT_LINK
from yacut.models import URLMap


def get_unique_short_id():
    random_symbol = string.ascii_letters + string.digits
    while True:
        short = ''.join(
            choice(random_symbol) for _ in range(
                NUMBER_OF_CHARACTERS_TO_GENERATE_SHORT_LINK
            )
        )
        if not URLMap.query.filter_by(short=short).first():
            break
    return short