from organizer import FileOrganizer

folder = input("Enter folder path: ")

organizer = FileOrganizer(folder)
count = organizer.organize()

print(f"{count} files organized successfully!")