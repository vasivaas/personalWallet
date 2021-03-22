"""Module for custom errors"""


class Error(Exception):
    """Base class for other errors"""
    pass


class PositiveNumberError(Error):
    """error for fields of integers less than 0"""

    def __str__(self):
        return 'The amount of money must greater than 0'


class LengthError(Error):
    """Error for length to string fields (e.g. full name, password)"""
    def __init__(self, min_length=1):
        self.__minimal_length = min_length

    def __str__(self):
        return f'The minimum length must be {self.__minimal_length} characters'


class FormatError(Error):
    """Incorrect data format error"""
    def __init__(self, field_name, format_msg):
        self.__field_name = field_name
        self.__msg = format_msg

    def __str__(self):
        return f'The {self.__field_name} must contain {self.__msg}'
