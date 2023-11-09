"""
    Module for testing 'pyutils.cli.flag'
"""
import pyutils.cli.flags as flag

# Test Setup and Teardown
def setup_module(module):
    """ Setup for the entire module """
    flag.flags.clear() # Ensure flags dictionary is clear before each test module

def teardown_module(module):
    """ Teardown for the entire module """
    flag.flags.clear() # Clear the flags after all tests run

# Test Cases
def test_process_args_no_values():
    """Test processing args without values"""
    flag.process_args(["--flag"])
    assert flag.verify_flag("--flag")
    assert flag.get_flag("--flag") == []

def test_process_args_with_values():
    """Test processing args with values"""
    flag.process_args(["--arg", "value"])
    assert flag.verify_flag("--arg")
    assert flag.get_flag("--arg") == "value"

def test_verify_flag():
    """Test the verification of flags"""
    flag.process_args(["--test"])
    assert flag.verify_flag("--test")
    assert not flag.verify_flag("--not_set")

def test_get_flag_default_value():
    """Test get_flag with a default value"""
    assert flag.get_flag("--missing", default_value="default") == "default"

def test_get_flag_with_prompt(monkeypatch):
    """Test get_flag with user prompt"""
    monkeypatch.setattr('builtins.input', lambda x: "user_input")
    assert flag.get_flag("--prompt", prompt_label="Enter value") == "user_input"


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
