from pathlib import Path
import pytest
from src.classifier import classify

@pytest.mark.parametrize("path, expected", [

    ("report.pdf", "Documents"),
    ("photo.jpg", "Images"),
    ("movie.mp4", "Videos"),
    ("song.mp3", "Audio"),
    ("unknown.xyz", None)
])

def test_classify(path, expected):

    result = classify(Path(path))
    
    assert result == expected
