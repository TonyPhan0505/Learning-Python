from collections import Counter

s = input()

t = input()

s_counts = Counter(s)

t_counts = Counter(t)

stickies = []

for key in s_counts.keys():

    if t_counts[key] > s_counts[key]:

        stickies.append(key)

print("".join(stickies))