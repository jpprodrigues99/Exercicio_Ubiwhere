import os
import django
import csv
from django.utils.dateparse import parse_datetime
from traffic.models import RoadSegment  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traffic_indicator.settings')  # Substitua 'traffic_indicator' pelo nome do seu projeto
django.setup()

def import_road_segments(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t') 
        for row in reader:
            RoadSegment.objects.create(
                long_start=float(row['Long_start']),
                lat_start=float(row['Lat_start']),
                long_end=float(row['Long_end']),
                lat_end=float(row['Lat_end']),
                length=float(row['Length']),
                speed=float(row['Speed'])
            )

if __name__ == '__main__':
    csv_file_path = '/traffic_indicator/traffic/traffic_speed.csv'  
    import_road_segments(csv_file_path)
