"""
Module for working with JSON files.
"""
import json


def write_to_file(filename, data, indent=4, encoding='utf-8'):
    """
    Write data to a JSON file.

    Args:
        filename (str): The path to the JSON file.
        data (Any): The data to be written to the file.
        indent (int, optional): The number of spaces to use for indentation. Defaults to 4.
        encoding (str, optional): The encoding to use for the file. Defaults to 'utf-8'.
    """
    with open(filename, 'w', encoding=encoding) as jsonfile:
        json.dump(data, jsonfile, indent=indent)


def read_json_file(filename):
    """
    Read data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        Any: The data read from the file.
    """
    with open(filename, 'r') as jsonfile:
        return json.load(jsonfile)
