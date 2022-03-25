
import pytest
import example1

def test_count_vowels_1():
    assert example1.count_vowels('reza hosseini VEDAD') == 8
    assert example1.count_vowels('reza hosseini') == 6
    assert example1.count_vowels('reza VEDAD') == 5

def test_count_vowels_2():
    assert example1.count_vowels('reza hosseini VEDAD') == 8
    assert example1.count_vowels('reza hosseini') == 7