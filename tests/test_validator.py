from src.validator import validate_folder

def test_validate_existing_folder(tmp_path):

    folder = tmp_path / "documents"
    folder.mkdir()
    result = validate_folder(folder)

    assert result == (True, "Valid folder")


def test_validate_file(tmp_path):
    
    file = tmp_path / "report.pdf"
    file.touch()
    result = validate_folder(file)
    
    assert result == (False, "Path is not a directory")


def test_validate_non_existing_path(tmp_path):
    
    path = tmp_path / "unknown_folder"
    
    result = validate_folder(path)
    
    assert result == (False, "Path doesn't exist")