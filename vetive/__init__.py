"""
    Module pou vetive
    - get_env_var
"""

from copy import deepcopy
import re
from itertools import repeat
from math import ceil, sqrt
import random
import os
import glob
from typing import Generator, List, Optional, Set
from xmlrpc.client import Boolean


def get_env_var(env_var_name: str) -> Optional[str]:
    """gets an environment variable"""
    env_var = os.environ.get(env_var_name)
    return env_var


def merge_sorted_lists(list1: List, list2: List) -> List:
    """returns a sorted merge of the provided list"""
    ell_one = deepcopy(list1)
    ell_two = deepcopy(list2)

    def _helper_generator():
        while ell_one or ell_two:
            if ell_one and ell_two:
                if ell_one[0] < ell_two[0]:
                    yield ell_one.pop(0)
                else:
                    yield ell_two.pop(0)
            elif ell_one:
                yield ell_one.pop(0)
            else:
                yield ell_two.pop(0)

    return list(_helper_generator())


def is_palindrome(word: str) -> bool:
    """Checks whether a word is a palindrome"""
    return word[::-1] == word


def is_prime(num: int) -> bool:
    """Checks if num is prime"""
    last_candidate = ceil(sqrt(num))
    answer = True
    if num == 2:
        answer = True
    else:
        for _ in range(2, 1 + last_candidate):
            if num % _ == 0:
                answer = False
                break
    return answer


def star_triangle(st_size: int) -> None:
    """return an appropriate size star triangle"""
    for _ in range(1, 1 + st_size):
        print("".join(repeat("*", _)))


def fibonacci_numbers(max_value: int = 100) -> Generator[int, None, None]:
    """generates Fibonacci Numbers up to the max value"""
    last_two = 0, 1
    if max_value == 0:
        yield last_two[0]
    else:
        yield last_two[0]
        while last_two[1] <= max_value:
            yield last_two[1]
            last_two = last_two[1], sum(last_two)


def words_from_corpus(directory_path: str) -> Generator[str, None, None]:
    """
    generates words from several text files (*.txt) under the directory,
    where a word is just a string of characters with no spaces, and a line
    is delimited by the return ('\n') character.
    """
    # list of syntax/symbols to ignore as part of a word
    # looping through the corpus directory
    for filepath in all_files_oftype(directory_path, "txt"):
        # opening the files
        with open(filepath, "r", encoding="utf-8") as file_reader:
            # reading each line of a file
            text = file_reader.readlines()
            for line in text:
                for word in re.sub(
                    r"\"|,|\'|\.|\n|\!|\-|\?", " ", line.strip()
                ).split():
                    yield word


def all_files_oftype(directory_path, extension: str) -> List[str]:
    """returns a list of all files in a directory ending with the provided extension"""
    return glob.glob(f"{directory_path}/*.{extension}")


def konte1a10():
    """fonksyon sa a konte de 1 a 10"""
    for _ in range(1, 11):
        print(_)


def random_digit_string(length: int = 6):
    """return a string of random digits"""
    return str(random.randint(1, 10**length)).zfill(length)
