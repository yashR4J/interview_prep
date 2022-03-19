# from json import load, dump

# try:
#     with open('a.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError:
#     with open('a.txt', 'w') as newFile:
#         newFile.write("This is the first line!")
#     with open('a.txt', 'r') as file:
#         print(file.read())

# try:
#     file = load(open("sample.json"))
#     print(file)
# except FileNotFoundError:
#     jsonDump = {"country_of_origin": "India",
#                 "country_of_citizenship": "Australia",
#                 "country_of_residence": "Australia"}
#     with open('sample.json', 'w') as file:
#         dump(jsonDump, file)
#     file = load(open("sample.json"))
#     print(file)
import csv
# with open('employeeBirthday.txt', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

with open('employeeBirthday.csv', 'w') as employee_file:
    # employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # employee_writer.writerow(['Name', 'Department', 'Birthday Month'])
    # employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    # employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer = csv.DictWriter(employee_file, ['Name', 'Department', 'Birthday Month'])
    employee_writer.writeheader()
    employee_writer.writerows([
        {'Name': 'John Smith', 'Department': 'Accounting', 'Birthday Month': 'November'},
        {'Name': 'Erica Meyers', 'Department': 'IT', 'Birthday Month': 'March'}
    ])

with open('employeeBirthday.csv', 'r') as employee_file:
    # csv_reader = csv.reader(employee_file, delimiter=",")
    # line_count = 0
    # for row in csv_reader:
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #     line_count += 1
    # print(f'Processed {line_count} lines.')

    csv_reader = csv.DictReader(employee_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        print(f'\t{row["Name"]} works in the {row["Department"]} department, and was born in {row["Birthday Month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')