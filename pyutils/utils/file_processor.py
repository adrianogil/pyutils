import os


def process_files_in_directory(path, extension, callback):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                note_path = os.path.join(root, file)
                callback(note_path)


def find_file(root_path, target_filename):
    """
    Recursively search for a file with the given target_filename starting from root_path.
    Returns the full path if found, otherwise returns None.
    """
    try:
        with os.scandir(root_path) as it:
            for entry in it:
                if entry.is_file() and entry.name == target_filename:
                    return entry.path
                elif entry.is_dir():
                    result = find_file(entry.path, target_filename)
                    if result:
                        return result
    except PermissionError:
        # Skip directories that cannot be accessed
        pass
    return None
