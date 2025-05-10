# splice_move_and_rename_file.py
import os
import shutil
from datetime import datetime

def move_and_rename_files(
    # input_folder=r"C:\Users\Myles\OneDrive\Documents\Xfer\Serum Presets\Presets\Splice",
    input_folder=r"C:\Users\Myles\Documents\Xfer\Serum Presets\Presets\Splice",
    # output_folder=r"C:\Users\Myles\OneDrive\Documents\Xfer\Serum Presets\Presets\Splice"
    output_folder=r"C:\Users\Myles\OneDrive\Documents\Xfer\Serum 2 Presets\Presets\S1 Presets\Splice"
    # output_folder=r"C:\Users\Myles\OneDrive\Documents\Xfer\Serum 2 Presets\Presets\S1 Presets\Splice"
):
    if not input_folder:
        input_folder = os.getcwd()

    today_str = datetime.today().strftime('%Y%m%d')

    file_count = 0
    deleted_dir_count  = 0
    
    # Create set of all dest filenames, stripped of any date prefix
    existing_files = set()
    if os.path.exists(output_folder):
        for f in os.listdir(output_folder):
            if os.path.isfile(os.path.join(output_folder, f)):
                if len(f) > 9 and f[:8].isdigit() and f[8] == "_":
                    existing_files.add(f[9:])  # Strip date prefix
                else:
                    existing_files.add(f)

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            old_path = os.path.join(root, file)

            if not os.path.isfile(old_path):
                continue

            # Check if this file (without timestamp) already exists in dest
            if file in existing_files:
                print(f"Skipping already existing file: {file}")
                continue

            # Name it with today's date, unless it already has one
            if len(file) > 8 and file[:8].isdigit() and file[8] == "_":
                new_filename = file  # Already timestamped
            else:
                new_filename = f"{today_str}_{file}"

            new_path = os.path.join(output_folder, new_filename)
            shutil.move(old_path, new_path)
            print(f"Moved: {old_path} -> {new_path}")
            file_count += 1

    print(f"Total files moved: {file_count}")

    # After moving all files, delete everything left in input_folder
    for root, dirs, files in os.walk(input_folder, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                print(f"Error deleting file {file}: {e}")
        for dir in dirs:
            try:
                os.rmdir(os.path.join(root, dir))
                print(f"Removed directory: {os.path.join(root, dir)}")
                deleted_dir_count += 1
                
            except Exception as e:
                print(f"Error deleting folder {dir}: {e}")
                
    print(f"Total directories deleted: {deleted_dir_count}")

if __name__ == "__main__":
    move_and_rename_files()
