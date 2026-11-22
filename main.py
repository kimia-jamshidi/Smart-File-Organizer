
from pathlib import Path
from src.validator import validate_folder
from src.scanner import scan_files
from src.classifier import classify
from src.organizer import organize_files


def main():
    user_input = input("input your path: ")
    path = Path(user_input)

    is_valid, message = validate_folder(path)

    if is_valid:
        try:
            files = scan_files(path)

            results = {}

            for file in files:
                category = classify(file)
                results[file] = category

            moved, skipped = organize_files(path, results)

            print("Moved:", moved, "Skipped:", skipped)

        except FileNotFoundError:
            print("Unable to scan the folder. The path no longer exists.")

    else:
        print(message)


if __name__ == "__main__":
    main()
