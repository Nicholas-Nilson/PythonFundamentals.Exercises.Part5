import string


def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = value.lower().replace(' ', '')
    return value == value[::-1]
