import csv

with open('gps_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    emp = []
    dic = {}
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if not (row[5] + ", " + row[6]) in emp:
                emp.append(row[5] + ", " + row[6])
                if not row[7] in dic.keys():
                    dic[row[7]] = []
                dic[row[7]].append(row[5] + ", " + row[6])
            
            line_count += 1
    print(f'Processed {line_count} lines.')
print(dic)