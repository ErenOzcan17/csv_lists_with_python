import csv
def veri_okuma():
    with open('1900_2021_DISASTERS.xlsx - emdat data.csv', newline='', encoding='utf-8') as csvfile:
        veri = csv.DictReader(csvfile, delimiter=',')

    return veri