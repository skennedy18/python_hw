import os 
import csv 

budget_data =  os.path.join("../" , "HW.csv")


with open(budget_data, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    print(f"header:{csv_header}")


    profit = []
    months = []

    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append(rows[0])

    rev_change = []

    for x in range (1, len(profit)):
        rev_change.append((int(profit[x]) - int(profit[x-1])))

    rev_average = sum(rev_change) / len(rev_change)

    total_months = len(months)

    greatest_inc = max(rev_change)
    greatest_dec = min(rev_change)

print("Financial Analysis")

print("_________________________________________________________________________")

print("total months: " + str(total_months))

print("Total: " + "$" + str(sum(profit)))

print("Average change: " + "$" + str(rev_average))

print("Greatest Increase in Profits: " + str(months[rev_change.index(max(rev_change))+1]) + " " + "$" + str(greatest_inc))

print("Greatest Decrease in Profits: " + str(months[rev_change.index(min(rev_change))+1]) + " " + "$" + str(greatest_dec))


file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(profit)) + "\n")

file.write("Average change: " + "$" + str(rev_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[rev_change.index(max(rev_change))+1]) + " " + "$" + str(greatest_inc) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[rev_change.index(min(rev_change))+1]) + " " + "$" + str(greatest_dec) + "\n")

file.close()
