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

#month by month changes in rev
all_changes = sum(revenue_changes)
avg_change = round(all_changes / (month_count - 1), 2)
greatest_increase = max(revenue_changes)
greatest_decrease = min(revenue_changes)
greatest_increase_month_index = revenue_changes.index(greatest_increase)
greatest_decrease_month_index = revenue_changes.index(greatest_decrease)
greatest_increase_month = month[greatest_increase_month_index + 1]
greatest_decrease_month = month[greatest_decrease_month_index + 1]
