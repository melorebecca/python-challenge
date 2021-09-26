 import os
import csv

#file path
csvpath = os.path.join('..','PyPoll','Resources', 'election_data.csv')


#variables
voterID = []
votes = 0


# read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)

        # loop 
        for row in csvreader: