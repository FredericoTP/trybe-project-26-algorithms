# Sobre o set:
# https://www.programiz.com/python-programming/set


def find_duplicate(nums):
    if len(nums) == 0:
        return False

    no_duplicates = set()

    for num in nums:
        if (type(num) is str) or num < 0:
            return False

        if num in no_duplicates:
            return num

        no_duplicates.add(num)

    return False
