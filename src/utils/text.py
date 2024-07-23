from pathlib import Path


def read_file_pathlib(file_path):
    return Path(file_path).read_text(encoding='utf-8')
