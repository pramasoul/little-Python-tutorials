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
    return 'FixMe'

def this_plus_that(a,b):
    """
    >>> this_plus_that(1,2)
    3
    >>> this_plus_that(109782357409,-123909876452)
    -14127519043
    >>> this_plus_that('foo', 'bar')
    'foobar'
    """
    return 'FixMe'

def triple(a):
    """
    >>> triple(7)
    21
    >>> triple('7')
    '777'
    """
    return 'FixMe'


def last_letter(s):
    """
    >>> last_letter("foobar")
    'r'
    >>> last_letter("x")
    'x'
    >>> last_letter("The quick brown fox jumped over the lazy dog.")
    '.'
    """
    return 'FixMe'
    
def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
