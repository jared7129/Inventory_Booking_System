import csv
import os

from django.core.management.base import BaseCommand
from Ibsapp.models import Inventory


class Command(BaseCommand):
    from Ibsapp.models import Member,Inventory,Booking

    def __parse_csv(self, reader):
        data = []
        headers = next(reader, None)
        for row in reader:
            _data = {}
            for h, v in zip(headers, row):
                if v == 'NULL':
                    v = ""
                _data[h.lower()] = v
            data.append(_data)
        return data

    def handle(self, *args, **options):

        with open('Inventory.csv') as f:
            reader = csv.reader(f)
            members = self.__parse_csv(reader)
        count = 0
        for member in members:
            inserted, err =Inventory.objects.update_or_create(id_no=member['id_no'], title=member['title'], description=member['description'], remaining_count=member['remaining_count'], expiration_date=member['expiration_date'])
            inserted.save()
        
        print('Updated inventory items')
