import zipfile
import os

def zip_files(file_paths, output_zip):
    """
    Zips a list of file paths into a single zip file.

    Args:
        file_paths (list of str): List of file paths to include in the zip file.
        output_zip (str): Path to the output zip file.
    """
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            if os.path.exists(file_path):
                # Add the file to the zip, preserving directory structure
                arcname = os.path.relpath(file_path, start=os.path.dirname(file_path))
                zipf.write(file_path, arcname)
            else:
                print(f"Warning: File not found - {file_path}")
    print(f"Files zipped successfully into: {output_zip}")
