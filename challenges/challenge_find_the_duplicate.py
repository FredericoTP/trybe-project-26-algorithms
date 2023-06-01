# Código do merge_sort baseado no mostrado no course
# Ciência da Computação - Seção 2 - Dia 3


def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)


def merge(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]

    left_i, right_i = 0, 0

    for index in range(start, end):
        if left_i >= len(left):
            array[index] = right[right_i]
            right_i += 1
        elif right_i >= len(right):
            array[index] = left[left_i]
            left_i += 1
        elif left[left_i] < right[right_i]:
            array[index] = left[left_i]
            left_i += 1
        else:
            array[index] = right[right_i]
            right_i += 1


def find_duplicate(nums):
    raise NotImplementedError
    # if len(nums) == 0:
    #     return False

    # numbers = nums
    # merge_sort(numbers, 0, len(numbers))

    # start = 1
    # stop = len(nums) - 1

    # while start <= stop:
    #     if type(numbers[start - 1]) is str or numbers[start - 1] < 0:
    #         return False
    #     if numbers[start] == numbers[start - 1]:
    #         return numbers[start]

    #     start += 1

    # return False
