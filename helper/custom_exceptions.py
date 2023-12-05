class NonPositiveIntegerException(Exception):
    def __init__(self):
        super().__init__('Exception: Only positive integers are allowed')

class StringBufferOverflowException(Exception):
    def __init__(self):
        super().__init__("The buffer for the string part shouldn't exceed the size of the string itself")
