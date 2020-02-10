import csv

with open('employee_file_1.csv', mode='w') as employee_file:
    fieldnames = ['name', 'dept', 'birth_month']
    employee_writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
    employee_writer.writeheader()
    employee_writer.writerow({'name': 'rupa', 'dept': 'cse', 'birth_month': 'jan'})
    employee_writer.writerow({'name': 'ram', 'dept': 'it', 'birth_month': 'jul'})
