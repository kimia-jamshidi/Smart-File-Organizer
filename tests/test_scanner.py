import pytest
from src.scanner import scan_files

def test_scan_files(tmp_path):
    folder = tmp_path / "downloads"
    folder.mkdir()

    (folder / "report.pdf").touch()
    (folder / "photo.jpg").touch()

    subfolder = folder / "Documents"
    subfolder.mkdir()

    files = scan_files(folder)

    assert set(files) == {
        folder / "report.pdf",
        folder / "photo.jpg"
    }


def test_scan_file_not_found(tmp_path):

    path = tmp_path / "unknown_folder"


    with pytest.raises(FileNotFoundError):
        scan_files(path)