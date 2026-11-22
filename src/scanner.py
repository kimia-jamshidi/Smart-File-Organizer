from pathlib import Path


def scan_files(path: Path) -> list[Path]:
    files = []

    for item in path.iterdir():
        if item.is_file():
            files.append(item)

    return files