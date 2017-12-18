from validate_email import checkmail
import csv

f = open('MatchResultFile2.csv')
csv_f = csv.reader(f)

myfile = open('myfile.csv', 'wb')
out = csv.writer(myfile, delimiter=',', lineterminator='\n')

# out = csv.writer(open("myfile.csv", "w"), delimiter=',', lineterminator='\n', )

for idx, row in enumerate(csv_f):
    code, message = checkmail(row[1])
    print(idx, code, message)
    out.writerow([row[1], code, message])
    myfile.flush()

myfile.close()
