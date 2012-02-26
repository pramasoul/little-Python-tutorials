"""
A few starting Python exercises.
http://docs.python.org/tutorial/ is a good reference
"""

def hello():
    """
    Say hello
    >>> hello()
    'Hello, world!'
    """
    return 'what goes here?'

def this_plus_that(a,b):
    """
    >>> this_plus_that(1,2)
    3
    >>> this_plus_that(109782357409,-123909876452)
    -14127519043
    >>> this_plus_that('foo', 'bar')
    'foobar'
    """
    return 'Wrong'

def triple(a):
    """
    >>> triple(7)
    21
    >>> triple('7')
    '777'
    """
    return 'Wrong'


def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
