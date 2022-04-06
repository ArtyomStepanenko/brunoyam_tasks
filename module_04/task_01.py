a = [1, 3, 4, 5, 6, 10]
element = 6

def binary_search(array, element, start, end):
	mid = int((start + end) / 2)
	if element == array[mid]:
		return mid
	elif element < array[mid]:
		return binary_search(array, element, start, mid - 1)
	else:
		return binary_search(array, element, mid + 1, end)

print(a)
print(binary_search(a, element, 0, len(a)))