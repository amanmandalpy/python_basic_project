import os
import hashlib


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except (PermissionError, OSError) as error:
        print(f"Could not read: {file_path}")
        print(f"Reason: {error}")
        return None


def find_duplicates(folder_path):

    file_hashes = {}

    total_files = 0

    print("\nScanning folder...\n")

    for root, directories, files in os.walk(folder_path):

        for filename in files:

            total_files += 1

            file_path = os.path.join(root, filename)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_path)

            else:
                file_hashes[file_hash] = [file_path]

    duplicates = []

    for files in file_hashes.values():

        if len(files) > 1:
            duplicates.append(files)

    print("=" * 60)
    print(f"Total Files Scanned: {total_files}")
    print(f"Duplicate Groups Found: {len(duplicates)}")
    print("=" * 60)

    if not duplicates:
        print("\nNo duplicate files found.")
        return

    print("\nDuplicate Files Found:")

    for group_number, files in enumerate(duplicates, start=1):

        print(f"\nGroup {group_number}")

        for file in files:
            print(f"  {file}")


folder = input("Enter folder path: ").strip()

if os.path.isdir(folder):
    find_duplicates(folder)
else:
    print("Invalid folder path.")
