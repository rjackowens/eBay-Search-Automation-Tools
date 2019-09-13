from textwrap import shorten

def trunc(x):
    x = shorten(x, width=50)
    return x
