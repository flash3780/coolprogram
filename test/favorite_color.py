import csv

with open('favorite_color.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    data = {}
    for row in reader:
        for field, value in row.iteritems():
            if not field in data:
                data[field] = [value]
            else:
                data[field].append(value)
data['correct_answers'] = [int(val) for val in data['correct_answers']]
boolval = {'true': True,
           'false': False}
data['cross_bridge'] = [boolval[val.lower()] for val in data['cross_bridge']]

# with open('favorite_color.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     data = []
#     for row in reader:
#         data.append(row)
