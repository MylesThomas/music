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

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            old_path = os.path.join(root, file)

            if not os.path.isfile(old_path):
                continue

            new_filename = f"{today_str}_{file}"
            
            # Check if already dated/timestamped
            if len(file) > 8 and file[:8].isdigit() and file[8] == "_":
                new_filename = file
                
            new_path = os.path.join(output_folder, new_filename)

            # os.makedirs(output_folder, exist_ok=True)

            shutil.move(old_path, new_path)
            # Print the old -> new path
            print(f"{old_path} -> {new_path}")
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
            except Exception as e:
                print(f"Error deleting folder {dir}: {e}")

if __name__ == "__main__":
    move_and_rename_files()
