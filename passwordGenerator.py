import string, random

def generate_password(length: int) -> str:
    """
    Generates a random password of a given length.

    The password will consist of a mix of uppercase and lowercase letters.
    If the length is less than or equal to 8, it will return an error message.

    Parameters:
    length (int): The length of the password to be generated.

    Returns:
    str: A random password of the given length or an error message.

    Example:
    >>> generate_password(12)
    'JGfEaRtYpLoKm'  # a random password of length 12
    >>> generate_password(5)
    'length should be greater than 8'
    """
    if length > 8:
        return "".join(random.choice(string.ascii_letters) for i in range(length))
    else:
        return "length should be greater than 8"



length = int(input("Enter the length of password :: "))
print(generate_password(length))