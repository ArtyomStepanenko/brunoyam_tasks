import unittest

def merge_sort(a):
	if len(a) < 2:
		return a[:]
	else:
		median = int(len(a) / 2)
		left = merge_sort(a[:median])
		right = merge_sort (a[median:])
		return merge(left, right)

def merge(left, right):
	res = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	while i < len(left):
		res.append(left[i])
		i += 1
	while j < len(right):
		res.append(right[j])
		j += 1
	return res

class TestMerge(unittest.TestCase):

	def test1(self):
		self.assertEqual(merge_sort([4, 5, 6, 10, 1, 3]), [1, 3, 4, 5, 6, 10])

	def test2(self):
		self.assertEqual(merge_sort([16, 2, 56, 15, 24]), [2, 15, 16, 24, 56])

unittest.main()