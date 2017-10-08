import csv

with open("epi_r.csv", "r") as source:
    rdr = csv.reader(source)
    with open("newfile.csv", "w") as result:
        wtr = csv.writer(result)
        for r in rdr:
            wtr.writerow((r[0], r[1], r[3], r[4]))

