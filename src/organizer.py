from pathlib import Path
import shutil

def organize_files(
    folder: Path,
    results: dict[Path, str | None]
) -> tuple[int, int]:


    moved = 0 
    skipped =0

    for file, category in results.items():

        if category is None:
            skipped += 1
            continue

        destination = folder / category
        destination.mkdir(exist_ok=True)

        destination_file = destination / file.name

        if destination_file.exists():
            skipped += 1
            continue

        shutil.move(file, destination_file)
        moved += 1

    return moved, skipped
        
