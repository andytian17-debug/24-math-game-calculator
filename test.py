Cmap = {
    'A' : 1,
    'J' : 11,
    'Q' : 12,
    'K' : 13,
}

S = input()
if S in Cmap:
    print(Cmap[S])
else:
    print(int(S))
