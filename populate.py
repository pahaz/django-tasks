import os
import django


def add_track(artist, title, url):
    track = Track.objects.get_or_create(artist=artist, title=title, url=url)[0]
    return track


def populate_music():
    artist = "Donna Lewis"
    title = "I Love You Always Forever"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Justin Martin"
    title = "Buggin"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Passenger"
    title = "Let Her Go"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Zeds Dead"
    title = "Hadouken"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Radiohead"
    title = "No Surprises"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Бутырка"
    title = "По этапу"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Хоттаб"
    title = "Салат"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Пиккадирска Терция"
    title = "Трамвай"
    add_track(artist=artist,
              title=title,
              url="/static/ogg/" + artist + " — " + title + ".ogg")

    artist = "Автор неизвестен"
    title = "Маленький трек"
    add_track(artist=artist,
              title=title,
              url="/static/mp3/" + artist + " — " + title + ".mp3")

    for t in Track.objects.all():
        print(str(t))


if __name__ == '__main__':
    print("Populating music...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_dont_stop.settings')
    django.setup()
    from music.models import Track
    populate_music()






