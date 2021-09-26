import os
import csv

#file path
csvpath = os.path.join('..','PyPoll','Resources', 'election_data.csv')

#define
def Poll(data):

        #variables
        total_votes = 0
        votes = []
        canidates = []
        unique_canidate = []
        winner = []

        #loop of data
        for row in data:

                #sum of votes
                total_votes += 1

                #append canidate names
                if row[2] not in unique_canidate:
                        unique_canidate.append(row[2])
                
                #list
                votes.append(row[2])

                #loop to find canidate, total votes, & vote percent calc
                for canidate in unique_canidate:
                        candidates.append(votes.count(canidate))
                        vote_percent.append(round(votes.count(canidate)/total_votes*100,3))

                #winner calc
                winner = unique_canidate[canidates.index(max(canidates))]

                #print 
                print ("Election Results")
                print ("-------------------------")
                print ("Total Votes: " + str(total_votes))
                print ("-------------------------")
                for i in range(len(unique_canidates)):
                        print (f"{unique_canidates[i]}: {vote_percent[i]}% {candidates[i]}")
                print ("-------------------------")
                print(f"Winner: {winner}")
                print ("-------------------------"

# write
output_file = os.path.join('..','PyPoll','Analysis', "election_analysis.txt")

with open(output_file, "w") as text:
        text.write("Election Results" + "\n")
        text.write("-------------------------" + "\n")
        text.write("Total Votes: " + str(total_votes) + "\n")
        text.write("-------------------------" + "\n")
        for i in range (len(unique_candidate)):
            txtfile.write(f"{unique_canidates[i]}: {vote_percent[i]}% {candidates[i]}") + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")   
    text.write("-------------------------" + "\n")


# read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)
        Poll(csvreader)
