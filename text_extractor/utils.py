import os


def is_valid_file(file_path):
    return os.path.isfile(file_path) and os.path.exists(file_path)
