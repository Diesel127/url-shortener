from database.crud import add_slug_to_db, get_long_url_by_slug
from shortener import generate_random_slug


async def generate_short_url(long_url: str):
    slug = generate_random_slug()
    await add_slug_to_db(slug, long_url)
    return slug

async def get_url_by_slug(slug: str) -> str:
    long_url = await get_long_url_by_slug(slug)
    if not long_url:
        raise ValueError("Slug not found") 
    return long_url
