from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import TitleGenre


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from genre_title.csv"

    def handle(self, *args, **options):

        if TitleGenre.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading genre_title data...")

        for row in DictReader(open(
            './static/data/genre_title.csv',
            encoding='utf-8',
            newline=''
        )):
            child = TitleGenre(
                id=row['id'],
                title_id=row['title_id'],
                genre_id=row['genre_id']
            )
            child.save()
        print("Successfully!")
