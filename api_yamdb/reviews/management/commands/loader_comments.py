from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Comments


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from comments.csv"

    def handle(self, *args, **options):

        if Comments.objects.exists():
            print('data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading comments data...")

        for row in DictReader(open('./static/data/comments.csv', encoding='utf-8', newline='')):
            child = Comments(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date'],
            )
            child.save()
        print("Successfully!")
