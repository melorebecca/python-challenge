import os
import csv

#file path
csvpath = os.path.join('..','PyPoll','Resources', 'election_data.csv')


#variables
voterID = []
total_votes = 0
canidate_votes = {}
canidate_percent = {}
win_votes = 0
wiiner = []


# read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)

        # loop 
        for row in csvreader: