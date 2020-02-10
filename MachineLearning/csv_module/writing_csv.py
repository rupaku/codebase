import csv
with open('employee_file.csv',mode='w') as employee_file:
    employee_writer=csv.writer(employee_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(['rupa','kumari','25'])
    employee_writer.writerow(['ram', 'kumar', '25'])