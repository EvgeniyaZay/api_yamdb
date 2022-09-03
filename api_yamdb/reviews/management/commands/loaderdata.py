import csv
import logging

from django.core.management import BaseCommand

from reviews.models import (
    Categories,
    Comments,
    Genres,
    TitleGenre,
    Review,
    Title
)
from user.models import (
    User
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

TABLES = {
    User: 'users.csv',
    Categories: 'category.csv',
    Genres: 'genre.csv',
    Title: 'titles.csv',
    TitleGenre: 'genre_title.csv',
    Review: 'review.csv',
    Comments: 'comments.csv',
}

replace_field = [
        'author',
        'category',
    ]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Loads data from csv files"

    def handle(self, *args, **kwargs):
        for model, csv_f in TABLES.items():
            with open(
                    f'./static/data/{csv_f}',
                    'r',
                    encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file, delimiter=',')
                for index, field in enumerate(reader.fieldnames):
                    if field in replace_field:
                        reader.fieldnames[index] += '_id'
                logger.info(f'Импорт данных в модель {model.__name__}.')
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Successfully!'))
