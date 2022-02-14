import csv

with open('accounts.csv', 'r') as file:
    csv_reader = csv.DictReader(file, delimiter='|')
    lc = 0
    res = []
    header = []
    for row in csv_reader:
        if lc == 0:
            header = row.keys()
            print(f"Columns are \n{' '.join(row)}")
        if row not in res:
            res.append(row)
        print(f"{row['AccountNumber']}\t\t{row['FirstName']}\t{row['LastName']}\t\t{row['AccountBalance']}\t{row['LastPaymentAmount']}\t")
        lc += 1
        
    print(res)
    with open('accounts.csv', 'a') as writeFile:
        csv_writer = csv.DictWriter(writeFile, header,delimiter='|')
        # csv_writer.writeheader()
        csv_writer.writerows(res)
        csv_writer.writerows([{'AccountNumber': '1001',
                              'FirstName': ' Cosmo',
                              'LastName': ' Kramer',
                              'AccountBalance': ' 5827.48',
                              'LastPaymentAmount': ' 1500.00'
                            },
                            {'AccountNumber': '1201',
                              'FirstName': ' Mosmo',
                              'LastName': ' Kramer',
                              'AccountBalance': ' 1241.25',
                              'LastPaymentAmount': ' 1241.05'
                            }])
        
