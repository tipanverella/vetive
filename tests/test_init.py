""" tests for init"""

from vetive import (
    fibonacci_numbers_generator,
    get_env_var,
    is_palindrome,
    is_prime,
    merge_sorted_lists,
)


def test_get_env_var():
    """test of get_env_var"""
    ev_home = get_env_var("HOME")
    ev_user = get_env_var("USER")
    ev_hsu = get_env_var("HOMESHELLUSER")
    assert ev_home is not None
    assert ev_user is not None
    assert ev_hsu is None


def test_merge_sorted_lists():
    """test of merge_sorted_lists"""
    list1 = [1, 4, 5, 5, 6]
    list2 = [2, 7, 11, 12, 12, 13]
    expected_output = [1, 2, 4, 5, 5, 6, 7, 11, 12, 12, 13]
    output = merge_sorted_lists(list1, list2)
    assert output == expected_output
    output = merge_sorted_lists(list2, list1)
    assert output == expected_output
    output = merge_sorted_lists(list1, [])
    assert output == list1
    output = merge_sorted_lists([], list2)
    assert output == list2
    output = merge_sorted_lists([], [])
    assert output == []


def test_is_palindrome():
    """test of is_palindrome"""
    assert is_palindrome("Tipan") == False
    assert is_palindrome("madam") == True
    assert is_palindrome("aaaaaaa") == True
    assert is_palindrome("street") == False


def test_fibonacci_numbers_generator():
    """test fibonacci_numbers_generator"""
    assert list(fibonacci_numbers_generator(0)) == [
        0,
    ]
    assert list(fibonacci_numbers_generator(1)) == [0, 1, 1]
    assert list(fibonacci_numbers_generator(2)) == [0, 1, 1, 2]
    assert list(fibonacci_numbers_generator(3)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_numbers_generator(4)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_numbers_generator(88)) == [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
    ]


def test_is_prime():
    """test is_prime"""
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(23)
    assert not is_prime(12345)
    assert is_prime(12347)
