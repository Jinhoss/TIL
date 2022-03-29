A = [5, 3, 1, 2, 7, 8, 6, 10, 13, 12, 15]
import time



def bubble_sort(arr):
	l = len(arr)
	for i in range(l - 1, 0, -1):
		for idx in range(i):
			if arr[idx] > arr[idx + 1]:
				arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
	return arr

def bubble_sort2(arr):
	l = len(arr)
	for i in range(l - 1, 0, -1):
		change = False
		for idx in range(i):
			if arr[idx] > arr[idx + 1]:
				change = True
				arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
		if not change:
			break
	return arr
			
# start = time.time()

# print(bubble_sort(A))

# end = time.time()

# print(f'{end - start} sec')

start = time.time()

print(bubble_sort2(A))

end = time.time()

print(f'{(end - start) * 100} sec')