"""
This script converts all video files in a 
specified folder to audio files using ffmpeg.
"""

import os
import sys
import subprocess

# Log file name
LOG_FILENAME = "converted.log"

# Common video file extensions
VIDEO_EXTENSIONS = [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"]

def is_video_file(filename):
    """Check if the given filename has a video file extension."""
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)

def convert_video_to_audio(input_path, output_path):
    """Convert a video file to an audio file using ffmpeg."""
    try:
        print(f"Converting: {input_path} to {output_path}")
        subprocess.run([
            "ffmpeg",
            "-i", input_path,
            output_path
        ], check=True)
        print(f"Converted: {input_path} → {output_path}")
        return True
    # Catch errors during conversion
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert: {input_path}\n{e}")
        return False

if __name__ == "__main__":
    folder_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    # Path to the log file
    log_path = os.path.join(folder_path, LOG_FILENAME)

    # Read already converted files from log
    converted_files = set()
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as log_file:
            for line in log_file:
                converted_files.add(line.strip())

    # Open log file for appending
    with open(log_path, "a", encoding="utf-8") as log_file:
        # Loop through all files in the specified folder
        for filename in os.listdir(folder_path):
            if is_video_file(filename):
                video_path = os.path.join(folder_path, filename)
                base_name = os.path.splitext(filename)[0]
                audio_path = os.path.join(folder_path, base_name + ".mp3")

                # Use relative path for log (just filename)
                if filename in converted_files or os.path.exists(audio_path):
                    print(f"⏭️ Skipping (already exists or logged): {audio_path}")
                    continue

                success = convert_video_to_audio(video_path, audio_path)
                if success:
                    log_file.write(filename + "\n")
                    log_file.flush()
