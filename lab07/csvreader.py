import csv

d = []

with open('../lab06/aggregation_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        d.append(int(row['doc_count']))
    csvfile.close()

print(d)