from math_series import __version__
from math_series.math_series import fibonacci,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_0():
    expected=0
    actual= fibonacci(0)
    assert expected==actual

def test_fibonacci_1():
    expected=1
    actual=fibonacci(1)
    assert expected==actual

def test_fibonacci_4():
    expected=3
    actual=fibonacci(4)
    assert expected==actual

def test_lucas_2():
    expected=2
    actual= lucas(2)
    assert expected==actual

def test_lucas_1():
    expected=1
    actual=lucas(1)
    assert expected==actual

def test_lucas_4():
    expected=5
    actual=lucas(4)
    assert expected==actual

def test_sum_series_4_a():
    expected=3
    actual=sum_series(4,0,1)
    assert expected==actual

def test_sum_series_4_b():
    expected=5
    actual=sum_series(4,2,1)
    assert expected==actual

def test_sum_series_4_c():
    expected=13
    actual=sum_series(4,2,3)
    assert expected==actual

def test_sum_series_4_d():
    expected=3
    actual=sum_series(4)
    assert expected==actual


