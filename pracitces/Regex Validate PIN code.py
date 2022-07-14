# ATM allow 4 or 6 digit PIN codes
# and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.Regex validate PIN code

# isdigit.() function 사용
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

# other way
def validate_pin(pin):
    """
    Returns True if pin is a string of 4 or 6 digits, False otherwise.
    """

    # First check that pin is a string of length 4 or 6
    if (type(pin) != str or len(pin) not in [4, 6]):
        return (False)

    # If any character is not a digit, return False
    for c in pin:
        if c not in "0123456789":
            return (False)

    # If all the characters are digits, return True
    return (True)