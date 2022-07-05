from re import L


def quick_sort(lst, start, end):
    if start >=end:
        return
    pivot = start
    left, right = start + 1, end

    while left<=right:
        while left<=end and lst[left] <= lst[pivot]:
            left += 1
        while right>start and lst[right]>=lst[pivot]:
            right-=1

        if left >right:
            lst[right], lst[pivot] = lst[pivot], lst[right]

        else:
            lst[right], lst[left] = lst[left], lst[right]
    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)

    return lst
    
print(quick_sort([5, 3, 2, 4, 7, 1, 8], 0, 6))