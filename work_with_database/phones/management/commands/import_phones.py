import csv
from django.http import HttpResponse
import json
import time
from django.core.management.base import BaseCommand
from phones.models import Phone
# from autoslug import AutoSlugField


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('work_with_database/phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:

            Phone(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
            ).save()
        return

