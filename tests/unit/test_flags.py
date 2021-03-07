"""
    Module for testing 'pyutils.cli.flag'
"""
import pyutils.cli.flags as flag

import pytest


def test_flags_verification():
    """Test whether flags are being detected"""
    flag.process_args(["--arg0", "--arg1", "a1", "--arg2", "b1", "b2", "--arg3", "c1", "c2", "c3", "--arg4", "d1", "d2", "d3"])
    assert flag.verify_flag("--arg0")
    assert flag.verify_flag("--arg1")
    assert flag.verify_flag("--arg2")
    assert flag.verify_flag("--arg3")
    assert flag.verify_flag("--arg4")
    assert not flag.verify_flag("--arg5")

# @testframework.test_description("Test whether args can be parameterized")
# def test_args_get_param(self):
#     argsutils.parse_args(["--arg0", "--arg1", "a1", "--arg2", "b1", "b2", "--arg3", "c1", "c2", "c3", "--arg4", "d1", "d2", "d3"])
#     self.assertEqual(argsutils.get_param("--arg1"), "a1")
