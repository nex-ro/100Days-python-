import csv
with open("weather_data.csv") as dataFile:
    temperature=[]
    dataCsv=csv.reader(dataFile)
    for i in dataCsv:
        if(i[1]!='temp'):
            temperature.append(i[1])
    print(temperature)

import pandas
