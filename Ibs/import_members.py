import csv

from django.core.management.base import BaseCommand


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

    def handle_noargs(self, *args, **options):

        with open('Members.csv') as f:
            reader = csv.reader(f)
            members = self.__parse_csv(reader)
        count = 0
        for member in members:
            count+=Member.objects.add(name=member['name'], surname=member['surname'], date_joined=['date_joined'], booking_count=['booking_count'])
        
        print('Updated {} members'.format(count))