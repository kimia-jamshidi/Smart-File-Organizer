from src.scanner import scan_files
from src.classifier import classify
from src.organizer import organize_files

def test_file_organizer_integration(tmp_path):
    folder = tmp_path / "downloads"
    folder.mkdir()

    (folder / "report.pdf").touch()
    (folder / "photo.jpg").touch()
    (folder / "unknown.xyz").touch()

    files = scan_files(folder)

    results = {}

    for file in files:
        category = classify(file)

        results[file] = category

    moved, skipped = organize_files(folder, results)



    assert moved == 2
    assert skipped == 1
    assert (folder / "Documents" / "report.pdf").exists()
    assert (folder / "Images" / "photo.jpg").exists()
    assert (folder / "unknown.xyz").exists()

