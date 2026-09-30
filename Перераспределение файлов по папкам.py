import os
import shutil
from pathlib import Path

SOURCE_DIR = Path("C:/Users/User/Downloads")

FILE_TYPES = {
    "Изображения": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp"],
    "Документы": [".pdf", ".docx", ".doc", ".xlsx", ".txt", ".pptx", ".pdf"],
    "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
}


def sort_files():
    if not SOURCE_DIR.exists():
        print(f"Ошибка: Папка {SOURCE_DIR} не найдена.")
        return

    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_file():
            file_ext = file_path.suffix.lower()
            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = SOURCE_DIR / folder_name
                    target_folder.mkdir(exist_ok=True)
                    try:
                        shutil.move(str(file_path), str(target_folder / file_path.name))
                        print(f"Перемещен: {file_path.name} -> {folder_name}/")
                    except Exception as e:
                        print(f"Ошибка при перемещении {file_path.name}: {e}")

                    moved = True
                    break

            if not moved:
                other_folder = SOURCE_DIR / "Другое"
                other_folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file_path), str(other_folder / file_path.name))
                    print(f"Неизвестный тип: {file_path.name} -> Другое/")
                except Exception as e:
                    print(f"Ошибка: {e}")

if __name__ == "__main__":
    sort_files()