'''test_capitalize

Generic pytest to test github actions
'''


def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()
