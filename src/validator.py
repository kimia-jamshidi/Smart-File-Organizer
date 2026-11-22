from pathlib import Path


def validate_folder(path: Path) -> tuple[bool, str]:
    if path.exists():
        if path.is_dir():
            return True, "Valid folder"
        else:
            return False, "Path is not a directory"
    else:
        return False, "Path doesn't exist"

