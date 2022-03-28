l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l_repeat = []

for i in l:
	if i not in l_repeat:
		n = 0
		for j in l:
			if i == j:
				n += 1
		if n >= 2:
			l_repeat.append(i)

print(l_repeat)