array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def counting_sort(arr):
	count = [0] * (max(array) + 1)
	
	for x in arr:
		count[x] += 1
	
	result = []
	for i in range(len(count)):
		for j in range(count[i]):
			result.append(i)

	return result

print(counting_sort(array))
