"""PlaceMelon: Your source for high-quality melon images on demand.

By Mel Melitpolski and Joel Burton <joel@joelburton.com>.
"""

import glob
from random import choice

from PIL import Image, ImageOps
from flask import Flask, render_template
from werkzeug.contrib.cache import MemcachedCache

from cachedecorator import cache


app = Flask(__name__)

# Our list of images in the images/ directory. These should all be JPEGs and, preferably,
# large and high-quality.
PHOTOS = glob.glob('images/*')

# We use Flask's simple, in-memory cache. This means this uses pre-generated images on
# server restart--but given that this is low-volume, that's fine.
img_cache = MemcachedCache(['127.0.0.1:11211'])


@app.route('/')
def homepage():
    return render_template('index.jinja.html')


@app.route('/<int:x>/<int:y>')
@cache(expires=3600)  # 1 hour
def photo(x, y):
    """Generate an image with size(x,y) and return it.

    Looks for an image of that size in the cache already. If there isn't one, it
    generates one from a random image in `images/` and then stores it in the
    cache.

    In any event, this returns a image/jpg image.
    """

    key = "%s-%s" % (x, y)
    data = img_cache.get(key)

    if not data:
        # Nothing found in cache; generate

        photo = choice(PHOTOS)

        with Image.open(photo) as img:
            img = ImageOps.fit(img, (x, y))
            data = img.tobytes('jpeg', img.mode)

        img_cache.set(key, data)

    return data, 200, {'Content-Type': 'image/jpeg'}


if __name__ == '__main__':
    # In production, this will run behind a real WSGI server; when started as a
    # script, start in debug mode.
    app.run(debug=True)