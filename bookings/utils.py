import random
import string
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_revenue_code_generator(instance, new_slug=None):
    if new_slug is not None:
        revenue_code = new_slug
    else:
        revenue_code = slugify(
            f'{instance.space}-{random_string_generator(size=4)}')
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(revenue_code=revenue_code).exists()
    if qs_exists:
        new_slug = f'{revenue_code}-{random_string_generator(size=4)}'
        return unique_revenue_code_generator(instance, new_slug=new_slug)
    return revenue_code
