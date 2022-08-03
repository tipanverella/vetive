"""
    Module pou vetive
    - get_env_var
"""

from copy import deepcopy
import os
from typing import List, Optional


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
