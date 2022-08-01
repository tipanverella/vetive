"""
    Module pou vetive
    - get_env_var
"""

import os
from typing import Optional, Union


def get_env_var(env_var_name: str) -> Optional[str]:
    """gets an environment variable"""
    env_var = os.environ.get(env_var_name)
    return env_var
