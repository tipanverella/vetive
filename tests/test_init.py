""" tests for init"""

from vetive import get_env_var

def test_get_env_var():
    """test of get_env_var"""
    ev_home = get_env_var("HOME")
    ev_shell = get_env_var("SHELL")
    ev_user = get_env_var("USER")
    ev_hsu = get_env_var("HOMESHELLUSER")
    assert ev_home is not None
    assert ev_shell is not None
    assert ev_user is not None
    assert ev_hsu is None
