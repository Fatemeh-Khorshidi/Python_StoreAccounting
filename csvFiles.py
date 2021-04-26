
import csv

with open('tt.csv' ) as test_file:
    csv_reader = csv.reader(test_file)

    count = 0
    for row in csv_reader:
        if count ==0:
            print(f'column names are{",".join(row)}')
            count +=1
        else:
            print(f'\t{row[0]}')
            count +=1
