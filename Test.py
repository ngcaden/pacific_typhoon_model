import pandas as pd

dataset = pd.read_csv('clean_data.csv', low_memory=False)

def region_check(row):
    lat = row['LAT']
    lon = row['LON']
    
    if lat <= 30 and lat >= 13 and lon <= 153 and lon >= 120:
        row['REGION_CHECK'] = True
    else:
        row['REGION_CHECK'] = False

    print row['CycNo']

dataset.apply(region_check, axis = 1)
