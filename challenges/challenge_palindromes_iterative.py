def is_palindrome_iterative(word):
    if len(word) == 0:
        return False

    if len(word) == 1:
        return True

    is_palindrome = False
    low_index = 0
    high_index = len(word) - 1

    while high_index >= low_index:
        if word[low_index] == word[high_index]:
            is_palindrome = True
        else:
            is_palindrome = False

        low_index += 1
        high_index -= 1

    return is_palindrome
