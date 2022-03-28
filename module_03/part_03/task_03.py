def maxnum(lst):
	while lst != []:
		maxdig = 0
		for i in range(len(lst)):
			dig = lst[i]
			while dig >= 10:
				dig = dig // 10
			if dig > maxdig:
				maxdig = dig
				maxi = i
		print(lst[maxi], end='')
		del lst[maxi]

l1 = [56, 9, 11, 2]
l2 = [3, 81, 5]

print(l1)
maxnum(l1)
print('\n')
print(l2)
maxnum(l2)
