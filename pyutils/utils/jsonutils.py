import json


def write_to_file(
    filename,
    data,
    indent=4,
    encoding='utf-8'
):
    with open(filename, 'w', encoding=encoding) as jsonfile:
        json.dump(
            data,
            jsonfile,
            indent=indent
        )

def read_json_file(filename):
    with open(filename, 'r') as jsonfile:
        return json.load(jsonfile)
