from poetry_sample.utils.utils_file import util_func
import pytest

def test_util_func(capsys):
    util_func()
    captured = capsys.readouterr()
    assert captured.out == "Hello from util\n"