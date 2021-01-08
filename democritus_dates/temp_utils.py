"""Utility functions temporarily provided until the rest of the democritus functions get uploaded."""

import functools


def number_zero_pad(num: int, length: int) -> str:
    """."""
    if length < len(str(num)):
        message = 'The length you provided is shorter than the number. Please provide a length that is at least as long as the given number.'
        raise ValueError(message)

    zero_padded_number = f'{num}'

    while len(zero_padded_number) < length:
        zero_padded_number = f'0{zero_padded_number}'

    return zero_padded_number


def date_parse_first_argument(func):
    """."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from dates_and_times import date_parse

        date_arg = args[0]
        other_args = args[1:]

        parsed_date_arg = date_parse(date_arg)
        return func(parsed_date_arg, *other_args, **kwargs)

    return wrapper
