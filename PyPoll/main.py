# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
votes = []
candidate_votes = []
str_candidates = ''

# Winning Candidate and Winning Count Tracker

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(".", end="")

        # Get the candidate's name from the row
        votes.append(row[2])

print('\n')

# Set total number of votes and list of candidates
vote_count = len(votes)
candidates = sorted(list(set(votes)))

# Determine number of votes per candidate
for i in candidates:
    candidate_votes.append((i,votes.count(i)))

    # Generating str_candidates variable
    if candidates.index(i) == len(candidates) - 1:
        str_candidates += f'{i}: {round(100*votes.count(i)/vote_count,3)}% ({votes.count(i)})'
    else:
        str_candidates += f'{i}: {round(100 * votes.count(i) / vote_count, 3)}% ({votes.count(i)})\n'

# Sort vote_counts list by number of votes (largest to smallest) to determine winner
candidate_votes.sort(key = lambda x:x[1], reverse=True)

#Generate output data and output string
str_total_votes = f'Total Votes: {vote_count}'

winner = f'Winner: {candidate_votes[0][0]}'

output = f'''Election Results
-------------------------
{str_total_votes}
-------------------------
{str_candidates}
-------------------------
{winner}
-------------------------'''

# Print the Election Results
print('\n' + output + '\n')

# Save the Election Results summary to the text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)