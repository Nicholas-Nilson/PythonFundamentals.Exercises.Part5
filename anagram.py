def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    # list_first = list(first_string).sort()
    # list_second = list(second_string).sort()
    return sorted(first_string) == sorted(second_string)