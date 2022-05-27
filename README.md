# Election_Analysis

## Overview of Election Audit
- The purpose of this audit was to determine the winner of the election and compute
a selection of statics including:
### Totals
    - Total votes counted
    - Votes received by each candidate
### Candidate stats
    - votes cast for each candidate
    - % of Total votes cast for each candidate
### Winner stats
    - Name/votes/percentage
### County stats
    - Votes cast in each county
    -% of Total votes cast in each county
    - County with the largest number of votes cast


## Election Audit Results:

- Total Votes Cast: 369,711
- Votes by county:
    
        Jefferson: 10.5% (38,855)
        
        Denver: 82.8% (306,055)
        
        Arapahoe: 6.7% (24,801)
- County with most ballots cast: Denver
- Candidate Results:

        Charles Casper Stockham: 23.0% (85,213)

        Diana DeGette: 73.8% (272,892)

        Raymon Anthony Doane: 3.1% (11,606)

- ## Winner:
        
        Winner: Diana DeGette
        
        Winning Vote Count: 272,892
        
        Winning Percentage: 73.8%

## Election Audit Summary:

    The automated process developed here (a python script) for analyzing election results could be applied to any election.
    The script ingests a preformatted csv file that contains three columns:
    - ballot id
    - County name
    - Candidate name
    The script iterates through each row in the file and counts total votes, while extracting unique candidate and county names with their respective vote counts.
    Once the totals have been tabulated the script computes percentages by candidate and county, as well as the election winner and county with most votes cast.
    
    The script could be modified in two ways to handle other elections:
    First, to support files with columns in different orders.
    Rather than hard coding positions for Candidate and County, we would read the header from the csv file and then find the position of the desired column in that list.
    For example:

```
    #reading the header
    header = next(reader)
    #then find the position of a desired column
    header.index('County')

```

    Second, to manage an election with requires a majority of votes to declare a winner, rather than the candidate with the most votes, we could modify the winner calculation as follows:

```

    #Change:
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    #to:
    if (vote_percentage > 50) and (vote_percentage > winning_percentage):
    ...
    else:
    'no winner'

```