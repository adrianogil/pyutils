
def capitalize(s):
    """
    Capitalizes the first letter of a string.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with the first letter capitalized.

    Examples:
        >>> capitalize('hello')
        'Hello'
        >>> capitalize('world')
        'World'
    """
    return s[0].upper() + s[1:]


def is_float(s):
    """
    Check if a given string can be converted to a float.

    Parameters:
    s (str): The string to be checked.

    Returns:
    bool: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    return False


def is_int(s):
    """
    Check if a given string can be converted to an integer.

    Args:
        s (str): The string to be checked.

    Returns:
        bool: True if the string can be converted to an integer, False otherwise.
    """
    try:
        int(s)
        return True
    except ValueError:
        pass

    return False


def get_random(l):
    from random import randint
    '''
    Returns a random element from the given list.

    Parameters:
        l (list): The list from which to select a random element.

    Returns:
        The randomly selected element from the list.
    '''
    return l[randint(0, len(l)-1)]
