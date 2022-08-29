from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Categories


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):

        if Categories.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Loading category data...")

        for row in DictReader(open('./static/data/category.csv', encoding='utf-8', newline='')):
            child = Categories(
              id=row['id'],
              name=row['name'],
              slug=row['slug']
            )
            child.save()
        print("Successfully!")
