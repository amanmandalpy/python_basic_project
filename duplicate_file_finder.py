import os
import hashlib


def calculate_hash(file_path):
    """Return SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def find_duplicate_files(folder_path):
    hash_dictionary = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            file_path = os.path.join(root, file)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in hash_dictionary:
                duplicates.append((file_path, hash_dictionary[file_hash]))
            else:
                hash_dictionary[file_hash] = file_path

    return duplicates


def main():

    folder = input("Enter folder path: ").strip()

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    duplicates = find_duplicate_files(folder)

    if duplicates:
        print("\nDuplicate Files Found\n")

        for duplicate, original in duplicates:
            print(f"Original : {original}")
            print(f"Duplicate: {duplicate}")
            print("-" * 50)

    else:
        print("\nNo duplicate files found.")


if __name__ == "__main__":
    main()