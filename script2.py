import csv
import requests
from pathlib import Path

with open('immovables_pics.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(spamreader):
        if index > 0:
            print(row[7])
            response = requests.get(row[7])
            if (response.ok):
                Path(f"img_files/{index}.jpg").write_bytes(response.content)