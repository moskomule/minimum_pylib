from numbers import Number
from typing import Union, Iterable


def _default_value(x):
    if isinstance(x, str):
        return "", str
    elif isinstance(x, Number):
        return 0, Number
    elif isinstance(x, list):
        return [], list
    else:
        raise TypeError("Unknown Type!")


def cum_add(*args: Iterable[Union[Number, list, str]]) -> Union[Number, list, str]:
    """
    Add given values

    :param *args: Arguments to be added.

    Example::

        cum_add("a", "b", "c")
        # abc

    """
    x, _type = _default_value(args[0])
    for v in args:
        if not isinstance(v, _type):
            raise TypeError(f"Expected {_type} but got {type(v)}")
        x += v
    return x
