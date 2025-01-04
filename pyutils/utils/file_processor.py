import os


def process_files_in_directory(path, extension, callback):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                note_path = os.path.join(root, file)
                callback(note_path)
