"""Utility to log video file names from a specified folder into 'converted.log'."""

import os
import sys

VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"]

def log_video_files(folder_path):
    """Logs names of video files in the specified folder to 'converted.log'."""
    log_file = "converted.log"
    folder_path = "../" + folder_path # move one directory up

    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    # Write matching filenames to log file
    log_file_path = os.path.join(folder_path, log_file)
    with open(log_file_path, "a", encoding="utf-8") as f:
        for entry in os.scandir(folder_path):
            if entry.is_file():
                _, ext = os.path.splitext(entry.name)
                if ext.lower() in VIDEO_EXTENSIONS:
                    f.write(entry.name + "\n")

    print(f"Finished. Matching filenames have been written to {log_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        folder = input("Enter the folder path to scan for video files: ").strip()
    else:
        folder = sys.argv[1]
        
    log_video_files(folder)
