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