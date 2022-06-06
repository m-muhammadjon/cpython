import inspect


def f():
    q = 1 + 2
    if q > 3:
        return 5
    return q


def get_source_code(f) -> str:
    s = inspect.getsource(f)
    q = '\n'.join(s.split('\n', 2)[1:])
    return q


get_source_code(f)
