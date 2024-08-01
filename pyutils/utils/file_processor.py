import os


def process_files_in_directory(path, extension, process_func):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                note_path = os.path.join(root, file)
                process_func(note_path)
