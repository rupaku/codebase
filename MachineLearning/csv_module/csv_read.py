import csv

with open('demo.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',quotechar='"')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are{", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department and was born in {row[2]}.')
            line_count += 1
        print(f'processed {line_count} lines.')
