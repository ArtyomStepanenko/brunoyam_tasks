from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)
maxel = 0

for j in m:
	for i in j:
		if i >= maxel:
			maxel = i

print(maxel)