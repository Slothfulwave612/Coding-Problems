## Dictionary and counter in Python to find winner of election
from collections import Counter

def election_winner(votes):
    '''
    Function to find out who won the elections.

    Argument:
    votes -- list, contaning all the votes by candidate name.

    Return:
    str, the candidate who won the election.
    '''
    votes_counter = Counter(votes)
    total_votes = []
    maxim_votes = votes_counter[max(votes_counter, key=votes_counter.get)]

    for i in votes_counter:
        if votes_counter[i] == maxim_votes:
            total_votes.append(i)
        
    print(sorted(total_votes)[0])

votes = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john'] 
election_winner(votes)
