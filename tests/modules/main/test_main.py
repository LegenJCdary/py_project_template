import pytest

from py_project_template.main import print_something


@pytest.mark.parametrize("string", [None, "", "something"])
def test_print_something(string: str):
    assert print_something(string) is None
