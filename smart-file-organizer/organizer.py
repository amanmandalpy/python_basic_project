import os
import shutil

class FileOrganizer:
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def organize(self):
        moved_files = 0

        for file in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file)

            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()

                for category, extensions in self.FILE_TYPES.items():
                    if ext in extensions:
                        category_folder = os.path.join(
                            self.folder_path,
                            category
                        )

                        os.makedirs(category_folder, exist_ok=True)

                        shutil.move(
                            file_path,
                            os.path.join(category_folder, file)
                        )

                        moved_files += 1
                        break

        return moved_files