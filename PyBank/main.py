import os
import csv

#import csv file
budget_csv = os.path.join("..", "resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader, None)

    #Find total number of months
    month_counter = 0
    net_total = 0
    profit_loss = []
    month_change = []
    greatest_inc = 0
    greatest_dec = 0
    #loop through rows
    for row in csv_reader:

        month_counter += 1

        net_total += int(row[1])

        profit_loss.append(int(row[1]))

    for i in range(len(profit_loss) - 1):
        month_change.append((profit_loss[i + 1]) - (profit_loss[i]))

    average_change = round(sum(month_change)/len(month_change), 2)

   
    for i in range(len(month_change) - 1):
        if month_change[i] > greatest_inc:
            greatest_inc = month_change[i]
        else:
            greatest_inc = greatest_inc
        if month_change[i] < greatest_dec:
            greatest_dec = month_change[i]
        else:
            greatest_dec = greatest_dec


    print(greatest_inc)
    print(greatest_dec)
    print(month_counter)
    print(average_change)
    print(net_total)

#Calculate net total amount of "Profit/Losses" over the entire period

#Calculate changes in "Profit/Losses" over the entire period

# Find the average of Profit/Losses changes

#Identify greatest increase in profits (date and amount) over the entire period

#Identify greatest decrease in profits (date and amount) over the entire period