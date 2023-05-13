import os
import datetime
import math

from weather.models import Weather, Statistics
from django.core.management.base import BaseCommand, CommandError

from django.db import connection
import pandas as pd


class Command(BaseCommand):
    help = 'Uploads data to database'

    def handle(self, *args, **options):

        directory = 'IndiaWeather'

        # iterate through directory
        for datafile in os.listdir(directory):
            print(datafile)
            filenamelist = datafile.split(".")
            filename = filenamelist[0]
            print(filename)

            path = os.getcwd()
            print("Current Directory", path)

            # prints parent directory
            print(os.path.abspath(os.path.join(path,"IndiaWeather" ,datafile)))
            filepath = os.path.abspath(os.path.join(path,"IndiaWeather" ,datafile))
            # df = pd.read_csv(filepath ,sep = '\t', header=None)
            df = pd.read_csv(filepath ,sep = ',')
            # print(df)

            with connection.cursor() as cursor:
                for i in range(len(df)):
                    # print(df.iloc[i, 0], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4])
                    if df.iloc[i, 0] is not math.nan:
                        dateString = str(df.iloc[i, 0])
                        dateList = dateString.split("-")
                        day = int(dateList[0])
                        month = int(dateList[1])
                        year = int(dateList[2])
                        date = datetime.date(year, month, day)
                    else:
                        continue
                    if df.iloc[i, 3] is not math.nan:
                        maximumTemp = float(df.iloc[i, 3])
                    else:
                        continue
                    if df.iloc[i, 2] is not math.nan:
                        minimumTemp = float(df.iloc[i, 2])
                    else:
                        continue
                    if df.iloc[i, 4] is not math.nan:
                        precipitation = float(df.iloc[i, 4])
                    else:
                        continue
                    stateCode = str(filename).upper()

                    cursor.execute('''INSERT INTO weather_weather (date,
                    maximum_temp, minimum_temp, precipitation, state_code) VALUES
                    (%s, %s, %s, %s, %s)''', [date, maximumTemp, minimumTemp, precipitation, stateCode]
                    )

        with connection.cursor() as cursor:
            cursor.execute('''INSERT INTO weather_statistics (year, average_minimum, average_maximum, total_precipitation, state_code)
                    SELECT strftime('%Y', date), round(avg(minimum_temp),2), round(avg(maximum_temp),2), round(sum(precipitation),2), state_code
                    FROM weather_weather WHERE maximum_temp IS NOT NULL AND minimum_temp IS NOT NULL AND precipitation IS NOT NULL
                    GROUP BY strftime('%Y', date), state_code; ''')












