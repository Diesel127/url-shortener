import string
from secrets import choice

ALPHABET = string.ascii_letters + string.digits

def generate_random_slug():
    slug = ""
    for i in range(6):
        slug += choice(ALPHABET)
    return slug