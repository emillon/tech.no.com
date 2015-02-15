from flask import Blueprint
from flask import Response
import PyRSS2Gen

from podcast import podcast_entries

tcom = Blueprint('tcom', __name__)


@tcom.route('/')
def home():
    return 'Hello, world'


# Extracted from:
# https://github.com/DirkR/capturadio/blob/master/capturadio/rss.py
class ItunesRSS(PyRSS2Gen.RSS2):
    """This class adds the "itunes" extension (<itunes:image>, etc.)
    to the rss feed."""

    rss_attrs = {
        "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "xmlns:media": "http://search.yahoo.com/mrss/",
        "version": "2.0",
    }

    def publish_extensions(self, handler):
        # implement this method to embed the <itunes:*> elements
        # into the channel header.
        if self.image_url is not None:
            handler.startElement('itunes:image', {'href': self.image_url})
            handler.endElement('itunes:image')


@tcom.route('/podcast.xml')
def podcast_feed():
    rss = ItunesRSS(title='Michel Platiniste podcast',
                    link='http://tech.no.com',
                    description='The Michel Platiniste podcast',
                    items=podcast_entries(),
                    )
    url = 'http://images-mix.netdna-ssl.com/w/300/h/300/q/85'
    url += '/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg'
    rss.image_url = url
    resp = Response(rss.to_xml(encoding='utf-8'),
                    content_type='application/rss+xml')
    return resp
