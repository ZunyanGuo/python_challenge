import os
import csv

# Path to the election data CSV file
PyPoll_csv = os.path.join("Resources","election_data.csv")


# Define a function to return unique elements in a list
def unique(a):
    set = []
    for i in a:
        if i not in set:
           set.append(i)
    return set

# Open the election data CSV file for reading
with open(PyPoll_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    header = next(csvreader)
    # Initialize variables to store the total number of votes and list of candidates
    number_of_votes = 0
    candidates = []

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total number of votes
        number_of_votes += 1
         # Add the unique candidate's name to the list of candidates
        candidates.append(row[2])
    candidates_list = unique(candidates)

    print(candidates_list)

    # Initialize variables to store the number of votes and percentage of votes for each unique candidate
    vote1 = 0
    vote2 = 0
    vote3 = 0
    # Loop through each candidate in the list of candidates
    for i in candidates:
        # Increment the vote count for the candidate
        if str(i) == candidates_list[0]:
           vote1 += 1
        elif str(i) == candidates_list[1]:
           vote2 += 1
        else:
           vote3 += 1
     # Calculate the percentage of votes for each candidate
    percentage_of_vote1 = vote1 / number_of_votes
    percentage_of_vote2 = vote2 / number_of_votes
    percentage_of_vote3 = vote3 / number_of_votes
    
    # Create dictionaries to store information for each unique candidate
    vote1_info = {"name":str(candidates_list[0]),
             "total number of votes": vote1,
             "percentage of votes": percentage_of_vote1}
    vote2_info = {"name":str(candidates_list[1]),
             "total number of votes": vote2,
             "percentage of votes": percentage_of_vote2}
    vote3_info = {"name":str(candidates_list[2]),
             "total number of votes": vote3,
             "percentage of votes": percentage_of_vote3}
    # Print the election results to the terminal
    print(f'Election Results')
    print(f'--------------------------------------------')
    print(f'Total Votes: {number_of_votes}')
    print(f'--------------------------------------------')
    print(f'{vote1_info["name"]}: {vote1_info["percentage of votes"]*100:.3f}% ({vote1_info["total number of votes"]})')
    print(f'{vote2_info["name"]}: {vote2_info["percentage of votes"]*100:.3f}% ({vote2_info["total number of votes"]})')
    print(f'{vote3_info["name"]}: {vote3_info["percentage of votes"]*100:.3f}% ({vote3_info["total number of votes"]})')
    print(f'--------------------------------------------')
    if max(vote1,vote2,vote3) in vote1_info.values():
        print(f'Winner: {vote1_info["name"]}')
    elif max(vote1,vote2,vote3) in vote2_info.values():
        print(f'Winner: {vote2_info["name"]}')
    else:
        print(f'Winner: {vote3_info["name"]}')
    print(f'--------------------------------------------')

# Write results to a text file   
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("--------------------------------------------\n")
    txtfile.write(f"Total Votes: {number_of_votes}\n")
    txtfile.write("--------------------------------------------\n")
    txtfile.write(f"{vote1_info['name']}: {vote1_info['percentage of votes']*100:.3f}% ({vote1_info['total number of votes']})\n")
    txtfile.write(f"{vote2_info['name']}: {vote2_info['percentage of votes']*100:.3f}% ({vote2_info['total number of votes']})\n")
    txtfile.write(f"{vote3_info['name']}: {vote3_info['percentage of votes']*100:.3f}% ({vote3_info['total number of votes']})\n")
    txtfile.write("--------------------------------------------\n")
    if max(vote1,vote2,vote3) in vote1_info.values():
        txtfile.write(f"Winner: {vote1_info['name']}\n")
    elif max(vote1,vote2,vote3) in vote2_info.values():
        txtfile.write(f"Winner: {vote2_info['name']}\n")
    else:
        txtfile.write(f"Winner: {vote3_info['name']}\n")
    txtfile.write("--------------------------------------------\n")

    
        

        
    
    
        
           
    

    

    
    

    