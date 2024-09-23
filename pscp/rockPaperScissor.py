"""rock paper scissor - rps"""
def checker(ab_item): #a_item is the first ones, b_item = second
    """checking between rock, paper and scissor to return pts"""
    match ab_item: # a != b
        case "RS" | "PR" | "SP":
            return 1, 0 #return A and B points
        case "RP" | "PS" | "SR":
            return 0, 1 #return A and B points
        case _:
            return 0, 0 #draw case
def rps(battle):
    """calculate the battles between A and B"""
    A = B = 0
    for i in range(0, len(battle), 2):
        a, b = checker(battle[i]+battle[i+1]) #checking between two elements
        A += a
        B += b
    if A == B:
        print(f"DRAW {A}")
    elif A > B:
        print(f"A win {A}-{B}")
    elif B > A:
        print(f"B win {B}-{A}")
rps(input())
#PR PR RS SP
#01 23 45 67
