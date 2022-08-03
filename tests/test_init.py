""" tests for init"""

from vetive import get_env_var, merge_sorted_lists

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
    output = merge_sorted_lists(list1,list2)
    assert output == expected_output
    output = merge_sorted_lists(list2,list1)
    assert output == expected_output
