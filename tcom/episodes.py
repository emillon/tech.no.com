"""
Hardcoded list of episodes.
A DB would be better, but hey.
"""

import datetime
import PyRSS2Gen
from dateutil.tz import tzutc


# Extracted from:
# https://github.com/DirkR/capturadio/blob/master/capturadio/rss.py
class ItunesRSSItem(PyRSS2Gen.RSSItem):

    def publish_extensions(self, handler):
        if self.image_url is not None:
            handler.startElement('media:thumbnail', {'href': self.image_url})
            handler.endElement('media:thumbnail')


class Episode:
    def __init__(self, title, slug, description, pubDate):
        self.title = title
        self.slug = slug
        self.description = description
        self.pubDate = pubDate

    def to_rss_item(self):
        item = ItunesRSSItem(
            title=self.title,
            description=self.description,
            enclosure=make_enclosure(self.slug),
            pubDate = self.pubDate,
            )
        item.image_url = PICS[self.slug]
        return item


def make_enclosure(slug):
    url = 'http://tech.no.com/episode/{}/download'.format(slug)
    return PyRSS2Gen.Enclosure(url, enclosure_length(slug), 'audio/mpeg')


def enclosure_length(slug):
    return LENGTH[slug]


def entries():
    return [ep.to_rss_item() for ep in EPISODES]


EPISODES = [
    Episode(u'The Pomodoro Sessions - Episode 13',
     u'the-pomodoro-sessions-episode-13',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode, cold dub techno. I finished it with a lovely Moby remix which I hope you won't find out of place; I didn't.",
     datetime.datetime(2014, 5, 27, 7, 19, 23, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 12',
     u'the-pomodoro-sessions-episode-12',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode, a few minimal and progressive tracks.",
     datetime.datetime(2014, 5, 20, 11, 40, 7, tzinfo=tzutc()),
     ),
    Episode(u'Just Drift',
     u'just-drift',
     u'I started deep in the spectrum of electronic music, with progressive house. My initial goal was to cut it to 25min to make a pomodoro mix but it was just too intense.\r\nI could not leave it there.\r\n\r\nI hope you will enjoy this mix as much as I enjoyed putting it together.\r\n\r\n\u2665\r\nE.',
     datetime.datetime(2014, 4, 28, 12, 41, 39, tzinfo=tzutc()),
     ),
    Episode(u'Pas-modoro classique',
     u'pas-modoro-classique',
     u"Un pomodoro en forme de trait d'union entre la Renaissance et la musique classique contemporaine.",
     datetime.datetime(2014, 4, 24, 14, 5, 56, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 11',
     u'the-pomodoro-sessions-episode-11',
     u'Upset => Techno\r\n\r\n\u2665 \r\n\r\nMichel',
     datetime.datetime(2014, 4, 15, 7, 20, 26, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 10',
     u'the-pomodoro-sessions-episode-10',
     u'Spring => Tech house.\r\n\r\n\u2665\r\n\r\nMichel',
     datetime.datetime(2014, 4, 7, 8, 38, 3, tzinfo=tzutc()),
     ),
    Episode(u'Voyage, Voyages, le retour',
     u'voyage-voyages-le-retour',
     u"Yet another set for the tired lone traveller's headphones\r\n\r\n\u2665 & \u266b ,\r\n\r\nMichel",
     datetime.datetime(2014, 3, 25, 8, 21, 13, tzinfo=tzutc()),
     ),
    Episode(u'Sample & Funky',
     u'sample-funky',
     u'Artists love sampling other tracks. In this mix we jump from one track to another through a sample in common.',
     datetime.datetime(2013, 12, 3, 10, 20, 24, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 9',
     u'the-pomodoro-sessions-episode-9',
     u'A progressive mix of long electronic tracks to accomodate with low temperatures and snowy weather, from ambient to techno.',
     datetime.datetime(2013, 11, 25, 15, 11, 45, tzinfo=tzutc()),
     ),
    Episode(u'Voyage, voyages',
     u'voyage-voyages',
     u"A set for the tired lone traveller's headphones...",
     datetime.datetime(2013, 9, 30, 15, 1, 12, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 8',
     u'the-pomodoro-sessions-episode-8',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episodes marks the return of this mix series. Summer is over. Let's drown ourselves into a (small) ocean of deep dub techno. Don't forget to bring a towel!",
     datetime.datetime(2013, 9, 24, 8, 48, 14, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 7',
     u'the-pomodoro-sessions-episode-7',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is full of minimal techno, in an attempt to demonstrate that plic plic + pioup pioup = plic pioup plic pioup.",
     datetime.datetime(2013, 6, 6, 12, 55, 40, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 6',
     u'the-pomodoro-sessions-episode-6',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode is TECH HOUSE TIME !",
     datetime.datetime(2013, 5, 27, 21, 59, 9, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 5',
     u'the-pomodoro-sessions-episode-5',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nYou'll take a voyage to the biggest black-hole at the center of the galaxy. As you'll approach and traverse the singularity, time will stretch forever, but keep calm, it's all in your brain.",
     datetime.datetime(2013, 5, 20, 15, 59, 56, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 4',
     u'the-pomodoro-sessions-episode-4',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode ? It's made of deep and heavy techno !",
     datetime.datetime(2013, 5, 6, 7, 46, 28, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 3',
     u'the-pomodoro-sessions-episode-3',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series. \r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nIn this episode we dive deep in a world of dark techno with a few latino tech house sounds.",
     datetime.datetime(2013, 4, 26, 9, 35, 50, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 2',
     u'the-pomodoro-sessions-episode-2',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nThis episode will let you flow smoothly through your 25 minutes...",
     datetime.datetime(2013, 4, 25, 8, 17, 58, tzinfo=tzutc()),
     ),
    Episode(u'The Pomodoro Sessions - Episode 1',
     u'the-pomodoro-sessions-episode-1',
     u"The Pomodoro technique is a time management strategy in which you split tasks by 25 min intervals. As long as a mix from this series.\r\nLoad a Pomodoro Sessions episode, click play, work. When it's over, take a break!\r\n\r\nLather, rinse, repeat.\r\n\r\nhttp://en.wikipedia.org/wiki/Pomodoro_Technique",
     datetime.datetime(2013, 4, 24, 11, 52, 10, tzinfo=tzutc()),
     ),
    Episode(u'Pile ou face',
     u'pile-ou-face',
     u"Pile c'est progressive. Face c'est minimale. Un mix en diptyque et en st\xe9r\xe9o.",
     datetime.datetime(2012, 12, 18, 11, 40, 50, tzinfo=tzutc()),
     ),
    Episode(u'Minimal sunday',
     u'minimal-sunday',
     u'',
     datetime.datetime(2012, 11, 19, 10, 28, 13, tzinfo=tzutc()),
     ),
    Episode(u'Lunettes carr\xe9es, chemises \xe0 carreaux',
     u'lunettes-carrees-chemises-a-carreaux',
     u'On a tous un cot\xe9 hipster, aussi.\r\n\r\n\r\n<3\r\n\r\nMarty',
     datetime.datetime(2012, 11, 10, 13, 10, 56, tzinfo=tzutc()),
     ),
    Episode(u'Tokamix #2 - La Guerre contre les Machines',
     u'tokamix-2-la-guerre-contre-les-machines',
     u'Temp\xeate dans la nimposph\xe8re, les machines prennent le pouvoir et elles se servent de samplers radioactifs.',
     datetime.datetime(2012, 11, 6, 10, 17, 43, tzinfo=tzutc()),
     ),
    Episode(u'Warming up GreHack 2012',
     u'warming-up-grehack-2012',
     u"Played two hours during GreHack CTF's warm-up cocktail.\r\n\r\nhttp://grehack.org/",
     datetime.datetime(2012, 10, 21, 19, 17, 5, tzinfo=tzutc()),
     ),
    Episode(u'Liqueur forte ou caf\xe9 noir',
     u'liqueur-forte-ou-cafe-noir',
     u"Let's make summer a bit longer with this short mix of '80s edits and reworks.",
     datetime.datetime(2012, 10, 10, 21, 31, 18, tzinfo=tzutc()),
     ),
    Episode(u"Once you go in, you don't come out",
     u'once-you-go-in-you-dont-come-out',
     u'',
     datetime.datetime(2012, 9, 4, 9, 52, 13, tzinfo=tzutc()),
     ),
    Episode(u"Tout le monde s'amuse \xe0 115BPM",
     u'tout-le-monde-samuse-a-115bpm',
     u"Tout le monde s'amuse, tout le monde boit des grands cocktails.\r\nTout le monde a du disco, tout le monde est smooth.\r\n\r\n115 BPM, le sweet spot entre le chill et le conformisme du dancefloor.\r\n\r\nEnjoy.",
     datetime.datetime(2012, 7, 10, 23, 46, 39, tzinfo=tzutc()),
     ),
    Episode(u"Downpitch'd Summer",
     u'downpitchd-summer',
     u'Je sais pas vous, mais ici il fait chaud, lourd, orageux ... Alors ne d\xe9passons pas les 122BPM.\r\n\r\n<3\r\n\r\nMarty',
     datetime.datetime(2012, 7, 10, 22, 49, 52, tzinfo=tzutc()),
     ),
    Episode(u'Ping pong - Minitex',
     u'ping-pong-minitex',
     u'',
     datetime.datetime(2012, 4, 6, 10, 13, 36, tzinfo=tzutc()),
     ),
    Episode(u'GroovyBaby',
     u'groovybaby',
     u'La p\xeache !\r\n\r\n\r\nMarty',
     datetime.datetime(2012, 3, 29, 23, 4, 22, tzinfo=tzutc()),
     ),
    Episode(u'Smooth',
     u'smooth',
     u"L'ami du petit d\xe9jeuner sonore, feat. Smoothie La Tr\xe8s Tr\xe8s Smooth.\r\n\r\nD\xe9sol\xe9 pour les deux lancements bizarres dans le dernier tiers, le matos se fait vieux.\r\n\r\n\r\n<3\r\n\r\nMarty",
     datetime.datetime(2012, 3, 20, 23, 3, 3, tzinfo=tzutc()),
     ),
    Episode(u'Ode aux Nuits',
     u'ode-aux-nuits',
     u"Une s\xe9lection de la programmation de l'\xe9dition \xe9dition 2012 des Nuits Sonores .",
     datetime.datetime(2012, 3, 8, 10, 18, 50, tzinfo=tzutc()),
     ),
    Episode(u'Techno 06/2009',
     u'techno-062009',
     u'',
     datetime.datetime(2011, 12, 5, 14, 28, 27, tzinfo=tzutc()),
     ),
    Episode(u'Promo 02/2010',
     u'promo-022010',
     u'An "old" mix I found sitting between two mp3s \u263a',
     datetime.datetime(2011, 11, 17, 11, 49, 20, tzinfo=tzutc()),
     ),
    Episode(u'2999 seconds',
     u'2999-seconds',
     u'2999 seconds of techno, old & new.',
     datetime.datetime(2011, 11, 15, 7, 55, 17, tzinfo=tzutc()),
     ),
    ]


LENGTH = {
    'downpitchd-summer':                       106358467,
    'groovybaby':                               79936817,
    'just-drift':                               64490880,
    'liqueur-forte-ou-cafe-noir':               29255022,
    'lunettes-carrees-chemises-a-carreaux':     84813360,
    'minimal-sunday':                           54653568,
    'ode-aux-nuits':                           105249600,
    'once-you-go-in-you-dont-come-out':         54826080,
    'pas-modoro-classique':                     66767227,
    'pile-ou-face':                             57486720,
    'ping-pong-minitex':                       189446400,
    'promo-022010':                            113860440,
    'sample-funky':                             21660315,
    'smooth':                                   70748885,
    'techno-062009':                            35550467,
    'the-pomodoro-sessions-episode-10':         60142611,
    'the-pomodoro-sessions-episode-11':         60004445,
    'the-pomodoro-sessions-episode-12':         28018560,
    'the-pomodoro-sessions-episode-13':         29723904,
    'the-pomodoro-sessions-episode-1':          23695872,
    'the-pomodoro-sessions-episode-2':          46068526,
    'the-pomodoro-sessions-episode-3':          24498816,
    'the-pomodoro-sessions-episode-4':          49736330,
    'the-pomodoro-sessions-episode-5':          57525992,
    'the-pomodoro-sessions-episode-6':          48783586,
    'the-pomodoro-sessions-episode-7':          32264640,
    'the-pomodoro-sessions-episode-8':          24755328,
    'the-pomodoro-sessions-episode-9':          59897729,
    'tokamix-2-la-guerre-contre-les-machines': 102189008,
    'tout-le-monde-samuse-a-115bpm':            44971008,
    'voyage-voyages-le-retour':                138232859,
    'voyage-voyages':                           86278833,
    'warming-up-grehack-2012':                 233538950,
    '2999-seconds': 0,
     }


PICS = {
    u'the-pomodoro-sessions-episode-13': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/3bafe648-175a-46cf-b955-b63191df2060.png',
    u'the-pomodoro-sessions-episode-12': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/db974d0d-7853-4ad4-be5e-018293eaa467.png',
    u'just-drift': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/34fd7667-1344-462e-8df3-2b33124dd839.jpg',
    u'pas-modoro-classique': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
    u'the-pomodoro-sessions-episode-11': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/336ad8a5-b4ff-4371-815c-ea3e4f81538b.png',
    u'the-pomodoro-sessions-episode-10': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/19b92597-f3b4-46df-a4cb-06281ee8c644.png',
    u'voyage-voyages-le-retour': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/8d5f7979-7b29-467b-b289-c55462ca9729.jpg',
    u'sample-funky': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
    u'the-pomodoro-sessions-episode-9': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c9526b69-7091-4b15-af45-3b4347b93689.png',
    u'voyage-voyages': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/30754347-93c2-47b0-b99a-610bc1a8f055.jpg',
    u'the-pomodoro-sessions-episode-8': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/68461c3d-5666-460e-b8d8-af3225573d1a.png',
    u'the-pomodoro-sessions-episode-7': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/22b2aa06-7056-4bd7-85f5-31895982f1bd.png',
    u'the-pomodoro-sessions-episode-6': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/2afc6d84-11a1-43b5-a7df-930a1823acf4.jpg',
    u'the-pomodoro-sessions-episode-5': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/a2679fad-11ac-47a0-8aba-14dc4b3504d6.png',
    u'the-pomodoro-sessions-episode-4': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c03dfa13-845d-4b92-8a09-4d3b95107ee1.png',
    u'the-pomodoro-sessions-episode-3': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/b2cefd0b-4fdf-4ef5-bef2-2965c9c5e642.png',
    u'the-pomodoro-sessions-episode-2': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/58ebd413-907b-4725-a479-2a38d6ac5fc8.png',
    u'the-pomodoro-sessions-episode-1': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ad19fa7d-8404-4eda-9c52-03ebbb7d92cd.png',
    u'pile-ou-face': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ee78622a-1557-4ef7-b392-4b35f87c9b75.jpg',
    u'minimal-sunday': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/profile/17f0211d-20a1-417c-9901-4b2e6b4a4831.jpeg',
    u'lunettes-carrees-chemises-a-carreaux': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/71eb50f4-79af-4b5b-b086-09f7ee8dffbc.jpg',
    u'tokamix-2-la-guerre-contre-les-machines': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/b70ef5d4-e5da-4c9a-bb19-35d7758375c8.jpg',
    u'warming-up-grehack-2012': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/ccd2b410-2b66-43c1-8c62-735acb70dc5a.png',
    u'liqueur-forte-ou-cafe-noir': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/360d835f-2ed2-4ba7-a1c3-54bd9e5288d8.png',
    u'once-you-go-in-you-dont-come-out': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/6a548efa-f5d4-444f-adc2-458f583e8f35.jpg',
    u'tout-le-monde-samuse-a-115bpm': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/c26bc6e5-2b46-4966-8ade-08474bc62d6b.jpg',
    u'downpitchd-summer': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/cafd601a-0ce0-48e6-b57e-1e3b4bc766ee.jpg',
    u'ping-pong-minitex': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/f55c12e9-4e3f-4c8e-8938-39cd52026e7f.jpg',
    u'groovybaby': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/406f2050-257f-4987-b275-3d4279e3a8d3.jpg',
    u'smooth': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/d07ee824-f404-4c54-a721-5bd5027f41c3.png',
    u'ode-aux-nuits': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/92b6b957-b2a8-4009-b2ae-341bfe267f23.jpg',
    u'techno-062009': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/4598b3d0-1718-45f2-b68c-2e2b3354b188.jpg',
    u'promo-022010': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/1283a5f8-ce8b-4c0a-8c45-764143d7749d.jpg',
    u'2999-seconds': u'http://images-mix.netdna-ssl.com/w/300/h/300/q/85/upload/images/extaudio/347746e5-c524-4279-9b42-5fd9be23ce34.jpg',
}
