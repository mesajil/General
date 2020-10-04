

def solveGender(userName):
    return "CHAT WITH HER!" if len(set([c for c in userName])) % 2 == 0 else "IGNORE HIM!"


print(solveGender (input()))