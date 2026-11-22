from pathlib import Path

def classify(path: Path) -> str | None:
    categories = {
        ".pdf" : "Documents",
        ".docx" : "Documents",
        ".txt" : "Documents",

        ".jpg" : "Images",
        ".png" : "Images",

        ".mp4" : "Videos",

        ".mp3" : "Audio",

    }
    extension = path.suffix.lower()
    result = categories.get(extension)

    return result
