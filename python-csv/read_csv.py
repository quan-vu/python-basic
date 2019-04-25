import csv

filename = 'users.csv'

# Reading CSV Files With csv
print('\r\nReading CSV Files \n')

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{" | ".join(row)}'.upper())
            line_count += 1
        else:
            print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
            line_count += 1        
    print(f'Processed {line_count} lines.')


# Reading CSV Files Into a Dictionary
print('\r\nReading CSV Files Into a Dictionary \n')

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0    
    for row in csv_reader:
        if line_count == 0:
            print(f'{" | ".join(row)}'.upper())
            line_count += 1
        
        print(f'{row["firstname"]} | {row["lastname"]} | {row["email"]} | {row["phone"]}')
        line_count += 1        
    print(f'Processed {line_count} lines.')
            