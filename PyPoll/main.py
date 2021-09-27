# Import Module
import os
import csv

# file path
csvpath = os.path.join("Resources","election_data.csv")

#lists
candidate_list = []
candidate_name = []
vote_count = []
vote_percent = []

#define
def Poll(data):

    total_count = 0
    # loop
    for row in data:

        total_count = total_count + 1
        # append names
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        #total vote count
        vote_count.append(row[2])

    # loop canidates
    for candidate in candidate_name:
        # vote counts
        candidate_list.append(vote_count.count(candidate))
        # vote percentage
        vote_percent.append(vote_count.count(candidate)/total_count*100)

    #winner calc
    winner = candidate_name[candidate_list.index(max(candidate_list))]
    
    # print
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_count}')
    print('--------------------------------')
    for i in range(len(candidate_name)):
        print(f'{candidate_name[i]}: {round(vote_percent[i],4)}% ({candidate_list[i]})')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # write
    output_file = os.path.join("Analysis","election_results.txt")

    with open(output_file, "w") as text:
        text.write("Election Results" + "\n")
        text.write("-------------------------" + "\n")
        text.write("Total Votes: " + str(total_count) + "\n")
        text.write("-------------------------" + "\n")
        for i in range(len(candidate_name)):
                text.write(f'{candidate_name[i]}: {round(vote_percent[i],3)}% ({candidate_list[i]})' + "\n")
        text.write("-------------------------" + "\n")
        text.write(f'Winner: {winner}'+ "\n")
        text.write("-------------------------" + "\n")

# read csv
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    Poll(csv_reader)