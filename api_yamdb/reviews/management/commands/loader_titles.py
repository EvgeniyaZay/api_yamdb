from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Title


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from titles.csv"

    def handle(self, *args, **options):

        if Title.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading titles data...")

        for row in DictReader(open('./static/data/titles.csv')):
            child = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category']
            )
            child.save()
        print("Successfully!")
