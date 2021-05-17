import csv
from arquivo import abre_csv
iter_csv = abre_csv(file="candidatura.csv")
csv_1996 = csv.writer(open("eleicao_1996.csv", 'w'))
csv_2000 = csv.writer(open("eleicao_2000.csv", 'w'))
csv_2004 = csv.writer(open("eleicao_2004.csv", 'w'))

header = next(iter_csv)
csv_1996.writerow(header)
csv_2000.writerow(header)
csv_2004.writerow(header)
for row in iter_csv:
    if int(row[0]) == 1996:
        csv_1996.writerow(row)
    if int(row[0]) == 2000:
        csv_2000.writerow(row)
    if int(row[0]) == 2004:
        csv_2004.writerow(row)