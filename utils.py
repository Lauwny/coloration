import csv
lst_dpt = []
with open('dpt.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        lst_dpt.append(row[0])
        #print("neighbors['"+row[0]+"'] = ['"+row[1]+"'],['"+row[2]+"'],['"+row[3]+"'],['"+row[4]+"'],['"+row[5]+"'],['"+row[6]+"'],['"+row[7]+"']")
print(lst_dpt)