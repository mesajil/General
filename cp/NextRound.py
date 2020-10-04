

def calNumParticipantsNextRound (n, k, a):
    nParticipantsNextRound = 0
    for i in range (n):
        if ((a[i] == 0) or (nParticipantsNextRound >= k and a[i] != last)):
            break
        nParticipantsNextRound += 1
        last = a[i]

    return nParticipantsNextRound


n, k = map(int, input().split())
a = list(map(int, input().split()))

print (calNumParticipantsNextRound(n, k, a))