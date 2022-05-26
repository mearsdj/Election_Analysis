#add dependencies
import csv
import os

#assign variable for full path to file to be read
file_to_load=os.path.join('Resources','election_results.csv')

#assign variable for full path to file to be written
file_to_save=os.path.join('analysis','election_analysis.txt')

#initialize vote counter variable and candidate list
total_votes=0
candidate_options=[]

# Declare empty dict to hold names/votes
candidate_votes={}

#Winning Candidate and Count trackers
winning_candidate = ''
winning_count = 0 
winning_percentage = 0

#open election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyze data here
    file_reader=csv.reader(election_data)

    #read and print header row
    headers=next(file_reader)
    
    for row in file_reader:
        
        #add to the total vote count
        total_votes +=1
        
        #get the candidate name from each row
        candidate_name=row[2]
        
        #add the candidate name to the candidate list
        #if candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            #add to list if not found
            candidate_options.append(candidate_name)

            # 2. beging tracking candidate vote count
            candidate_votes[candidate_name] = 0

        #increment vote count by row
        candidate_votes[candidate_name] += 1

#determine percentage of total vote received by each candidate and print to screen
# for candidate in candidate_options:
    #print(f'Candidate {candidate} received {candidate_votes[candidate]/total_votes:.2%} of the total votes')

#1. iterate though dict
for candidate_name in candidate_votes:
    #get vote count
    votes=candidate_votes[candidate_name]

    # calc pct of votes
    vote_perecentage=float(votes)/float(total_votes)

    #add name/votes/pct to respective variables if largest
    if (votes>winning_count) and (vote_perecentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_perecentage
        winning_candidate=candidate_name
    
    print(f'{candidate_name}: {vote_perecentage:.1%} ({votes:,})\n')

winning_candidate_summary = (
    f'---------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1%}\n'
    f'----------------------------\n')
print(winning_candidate_summary)
