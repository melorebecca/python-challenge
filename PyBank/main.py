import os
import csv

#file path
csvpath = os.path.join('..','PyBank','Resources', 'budget_data.csv')

#lists/variables
month = []
month_count = 0
totalProfitLosses = 0
curMonthrev = 0
prevMonthrev = 0
total_revenue = 0
revenue_changes = []

# read csv file
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        csvheader = next(csvreader)

        # loop
        for row in csvreader:

            #list of the months
            month_count = month_count + 1
            month.append(row[0])
                       
            #total profit/losses
            totalProfitLosses += int(row[1])
            
            # month to month changes in rev
            curMonthrev = int(row[1])
            total_revenue = total_revenue + curMonthrev
            if month_count > 1:
                revenue_change = curMonthrev - prevMonthrev
                revenue_changes.append(revenue_change)
            prevMonthrev = curMonthrev