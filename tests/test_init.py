""" tests for init"""
import os
from os import makedirs, rmdir
import pathlib

from vetive.__init__ import (
    fibonacci_numbers,
    get_env_var,
    is_palindrome,
    is_prime,
    merge_sorted_lists,
    random_digit_string,
    all_files_oftype,
    is_part_of,
    words_from_corpus,
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
    assert list(fibonacci_numbers(0)) == [
        0,
    ]
    assert list(fibonacci_numbers(1)) == [0, 1, 1]
    assert list(fibonacci_numbers(2)) == [0, 1, 1, 2]
    assert list(fibonacci_numbers(3)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_numbers(4)) == [0, 1, 1, 2, 3]
    assert list(fibonacci_numbers(88)) == [
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


def test_words_from_corpus():
    """test words_from_corpus"""
    assert list(words_from_corpus("tests/corpus")) == [
        "Bonjour",
        "le",
        "monde!",
        "Hello",
        "world!",
        "Buenos",
        "dias!",
        "Comment",
        "allez",
        "vous?",
        "Je",
        "suis",
        "Dede",
        "Assann",
        "et",
        "j",
        "apprend",
        "a",
        "programmer",
        "avec",
        "Tipan",
        "Verella",
        "Il",
        "est",
        "un",
        '"Data',
        'scientist"',
        "et",
        "vit",
        "aux",
        "USA",
    ]


def test_is_part_of():
    """test is_part_of"""
    # preparing the tests
    list1 = []
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c"]
    set_ex = {2, "a", True}
    # testing the fonction
    assert is_part_of(1, list2) == True
    assert is_part_of(1, list1) == False
    assert is_part_of(1, list3) == False
    assert is_part_of("a", list1) == False
    assert is_part_of("a", list2) == False
    assert is_part_of("a", list3) == True
    assert is_part_of(True, set_ex) == True
    assert is_part_of("x", list3) == False
    ...


def test_all_files_oftype():
    """test all_files_oftype"""
    # empty directory
    tmp_dir_name = f"tmp_directory_{random_digit_string()}"
    makedirs(tmp_dir_name)
    assert all_files_oftype(tmp_dir_name, "txt") == []
    # directory with no files of the type
    assert all_files_oftype(tmp_dir_name, tmp_dir_name) == []
    # when there is stuff to return
    pathlib.Path(f"{tmp_dir_name}/all_files_oftype.txt").touch()
    assert all_files_oftype(tmp_dir_name, "txt") == [
        f"{tmp_dir_name}/all_files_oftype.txt"
    ]
    os.remove(f"{tmp_dir_name}/all_files_oftype.txt")
    rmdir(tmp_dir_name)


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
