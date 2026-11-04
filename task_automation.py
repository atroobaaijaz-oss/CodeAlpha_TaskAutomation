import os
import shutil

def organize_jpg_files():

    source_folder = "source_images"
    destination_folder = "organized_images"

    # Create destination folder if it does not exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Find and move all JPG files
    for filename in os.listdir(source_folder):

        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            shutil.move(source_path, destination_path)

            print(f"Moved: {filename}")

    print("All JPG files have been organized successfully!")


# Run the automation
organize_jpg_files()