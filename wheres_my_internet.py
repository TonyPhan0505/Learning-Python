import  collections

n, m = map(int, input().split())

AL = [[] for _ in range(n)]

for k in range(m):
	i, j = map(int, input().split())
	i -= 1
	j -= 1
	AL[j].append(i)
	AL[i].append(j)

seen = set()
queue = collections.deque()
queue.append(0)

while (len(queue) != 0):
	v = queue.popleft()
	seen.add(v)

	for u in AL[v]:
		if u not in seen:
			queue.append(u)

if len(seen) == n:
	print("Connected")

else:
	for i in range(n):
		if (i not in seen):
			print(i + 1)
