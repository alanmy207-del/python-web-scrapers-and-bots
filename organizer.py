import os
import shutil


def organize_directory(target_folder):
    print(f"[+] Scanning directory: {target_folder}")

    # File extension mappings
    categories = {
        "Documents": [".pdf", ".txt", ".csv", ".docx", ".json"],
        "Executables": [".exe", ".msi"],
        "Python_Scripts": [".py"],
    }

    files = [
        f
        for f in os.listdir(target_folder)
        if os.path.isfile(os.path.join(target_folder, f))
    ]

    moved_count = 0
    for file in files:
        # Avoid moving our active python scripts
        if file in [
            "scraper.py",
            "monitor.py",
            "organizer.py",
            "auth_demo.py",
            "da.py",
        ]:
            continue

        ext = os.path.splitext(file)[1].lower()
        for category, extensions in categories.items():
            if ext in extensions:
                folder_path = os.path.join(target_folder, category)
                os.makedirs(folder_path, exist_ok=True)

                src = os.path.join(target_folder, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)
                print(f"[->] Moved '{file}' to '{category}/'")
                moved_count += 1
                break

    print(f"[✓] Cleanup complete! Organized {moved_count} files.")


if __name__ == "__main__":
    # Organizes current working directory
    current_dir = os.getcwd()
    organize_directory(current_dir)