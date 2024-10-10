"""Majority"""
def majority(candidate_n, voter_n):
    """find the leader of the group"""
    candidate_n += 0
    election = {}
    for _ in range(voter_n):
        voter = int(input())
        election[voter] = election.get(voter, 0) + 1
    most = max(election.values())
    index = list(election.values()).index(most)
    key = list(election.keys())[index]
    if most > (1/2) * voter_n:
        print(key, most)
    else:
        print(0, most)
majority(int(input()), int(input()))
