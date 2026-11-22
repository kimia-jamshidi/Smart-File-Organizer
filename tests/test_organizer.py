
from src.organizer import organize_files


def test_organize_files(tmp_path):
    folder = tmp_path / "downloads"
    folder.mkdir()

    (folder / "report.pdf").touch()
    (folder / "unknown.xyz").touch()

    results ={
        folder / "report.pdf": "Documents",
        folder / "unknown.xyz": None
    }
    
    moved, skipped = organize_files(folder, results)

    assert moved == 1
    assert skipped == 1

    assert (folder / "Documents" / "report.pdf").exists()
    assert (folder / "unknown.xyz").exists()



def test_organize_empty_folder(tmp_path):
    folder = tmp_path / "downloads"
    folder.mkdir()

    results = {}

    moved, skipped = organize_files(folder, results)

    assert moved == 0
    assert skipped == 0



def test_organize_all_uncategorized(tmp_path):
    folder = tmp_path / "downloads"
    folder.mkdir()

    file1 = folder / "unknown.xyz"
    file2 =folder / "data.csv"
    file1.touch()
    file2.touch()

    results = {
        file1: None,
        file2: None
    }

    moved, skipped = organize_files(folder, results)

    assert moved == 0
    assert skipped == 2
    assert file1.exists()
    assert file2.exists()


def test_organize_duplicate_file(tmp_path):

    folder = tmp_path / "downloads"
    folder.mkdir()

    source_file = folder / "report.pdf"
    source_file.touch()

    destination = folder / "Documents"
    destination.mkdir()

    existing_file = destination / "report.pdf"
    existing_file.touch()

    results = {
        source_file: "Documents"
    }

    moved, skipped = organize_files(folder, results)

    assert moved == 0
    assert skipped == 1

    assert source_file.exists()
    assert existing_file.exists()
