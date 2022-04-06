a = [4, 5, 6, 10, 1, 3]

def insertion_sort(array):
	for i in range(1, len(array)):
		current = array[i]
		j = i - 1
		while j >= 0 and current < array[j]:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = current

print(a)
insertion_sort(a)
print(a)