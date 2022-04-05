def selection_sort(arr):
	l = len(arr)
	for i in range(l - 1):
		min_idx = i
		for j in range(i, l):
			if arr[j] < arr[min_idx]:
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]

	return arr

d = [2, 4, 5, 1, 3]

sort_d = selection_sort(d)

print(sort_d)