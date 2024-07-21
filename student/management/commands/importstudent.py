import pandas as pd

from django.core.management.base import BaseCommand
from student.models import Student
import os
from django.conf import settings


class Command (BaseCommand):
    help = "Import student data from csv file"

    def handle(self, *args, **kwargs):

        # define the path for data folder
        data_dir = os.path.join(settings.BASE_DIR, 'data')
        csv_file_path = os.path.join(data_dir, 'sample.csv')
        try:
            df = pd.read_csv(csv_file_path)
            
			# fill the missing value
            
            # df.fillna(0, inplace=True)    # this method fill all the empty field with 0
            df['name']=df['name'].fillna(value="Unknown")
            df['age']=df['age'].ffill()
            df['city']=df['city'].fillna(value="Unknown")
            
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File Not Found'))
            return

        for _, row in df.iterrows():
            print(row)
            # break
            Student.objects.create(
                name=row['name'],
                age=row['age'],
                city=row['city']
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully impported students.'
        ))
