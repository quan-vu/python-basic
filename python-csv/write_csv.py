import csv

# Writing CSV Files
with open('employees_1.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['fullname', 'department', 'birth_day'])
    writer.writerow(['John Smith', 'Accounting', '1990-01-01'])
    writer.writerow(['Quan Vu', 'IT', '1990-01-01'])

# Writing CSV Files from a Dictionary
with open('employees_2.csv', mode='w') as csv_file:
    field_names = ['firstname', 'lastname', 'department', 'birth_day']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'firstname': 'Quan', 'lastname': 'Vu', 'department': 'IT', 'birth_day': '1990-05-01'})
    writer.writerow({'firstname': 'John', 'lastname': 'Smith', 'department': 'HR', 'birth_day': '1988-01-01'})

