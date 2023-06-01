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


def is_anagram(first_string, second_string):
    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort(first_list, 0, len(first_list))
    merge_sort(second_list, 0, len(second_list))

    if (
        first_list == second_list
        and len(first_list) != 0
        and len(second_list) != 0
    ):
        return ("".join(first_list), "".join(second_list), True)

    return ("".join(first_list), "".join(second_list), False)
