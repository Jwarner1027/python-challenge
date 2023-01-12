import os
import csv

#import csv file
budget_csv = os.path.join("..", "resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader, None)

    #Define variables and empty lists
    month_total = 0
    net_total = 0
    month_list = []
    prof_loss = []
    month_change = []
    greatest_inc = 0
    greatest_dec = 0

    #loop through rows
    for row in csv_reader:

        #Find total months
        month_total += 1

        #Calculate net total for profit/loss
        net_total += int(row[1])

        #Add to new lists
        prof_loss.append(int(row[1]))
        month_list.append(row[0])

    #Loop through each value for prof_loss
    for i in range(len(prof_loss) - 1):

        #List of monthly changes
        month_change.append((prof_loss[i + 1]) - (prof_loss[i]))

    #Calculate average change
    average_change = sum(month_change)/len(month_change)

   #Loop through the monthly changes list to find greatest increase and greatest decrease
    for i in range(len(month_change) - 1):
        if month_change[i] > greatest_inc:
            greatest_inc = month_change[i]
        else:
            greatest_inc = greatest_inc
        if month_change[i] < greatest_dec:
            greatest_dec = month_change[i]
        else:
            greatest_dec = greatest_dec

    #Identify the profit value that led to greatest increase/ greatest decrease
    profit_value = prof_loss[month_change.index(greatest_inc) + 1]
    loss_value = prof_loss[month_change.index(greatest_dec) + 1]

    #Find the index in profit/loss list
    increase_index = prof_loss.index(profit_value)
    decrease_index = prof_loss.index(loss_value)

    #Identify greatest increase/decrease date matching that index in the month list
    increase_date =  month_list[increase_index]
    decrease_date = month_list[decrease_index]

#Print in text file
analysis = open("analysis.txt", 'w')
analysis.write("Financial Analysis\n")
analysis.write("-----------------------------\n")
analysis.write("Total Months: %d\n" % month_total)
analysis.write("Total $ %d\n" % net_total)
analysis.write("Average Change: $%d\n" % round(average_change, 2))
analysis.write("Greatest Increase in Profits: %s ($%s)\n" % (increase_date, greatest_inc))
analysis.write("Greatest Decrease in Profits: %s ($%s)" % (decrease_date, greatest_dec))