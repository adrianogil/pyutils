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
