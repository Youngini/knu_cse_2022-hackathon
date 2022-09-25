import csv
import os
from unicodedata import category
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assertive_prj.settings')
django.setup()

from main.models import Category,TourSpot,Option

def main():
    with open('category.csv' ,encoding='UTF8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader,None)
        for row in data_reader:
            categories = Category.objects.all()
            if len(row)==0: continue
            if row not in categories:
                Category.objects.create(
                    name = row[0],
                    slug = row[0]
                )



    with open('data.csv' ,encoding='UTF8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader,None)
        categories = Category.objects.all()
        for row in data_reader:
            for op in categories:
                if len(row)==0: continue
                if row[2]==str(op):
                    TourSpot.objects.create(
                        place = row[0],
                        location = row[1],
                        category = op,
                        mapX = row[3],
                        mapY = row[4],
                        like = False
                    )


    with open('withTrouble.csv',encoding='UTF8')as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader,None)

        for row in data_reader:
            print(row)
            if len(row)==0:continue
            for col in range(1,len(row)-1):
                if len(row[col])==0:continue
                Option.objects.create(
                    tourspot = TourSpot.objects.get(place = row[0]),
                    name = row[col],

                )


            




            




if __name__ == "__main__":
    main()