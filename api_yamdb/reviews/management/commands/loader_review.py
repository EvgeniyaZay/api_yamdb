from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Reviews


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from review.csv"

    def handle(self, *args, **options):

        if Reviews.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading review data...")

        for row in DictReader(open('./static/data/review.csv')):
            child = Reviews(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date']
            )
            child.save()
        print("Successfully!")