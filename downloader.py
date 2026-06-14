"""
This script downloads all the transcripts, summaries, and comments from the
Cozy Coding Hour GitHub repository.
"""
import os
import zipfile
import requests

def download_file(url, output_path):
    """
    Downloads a file from a URL and saves it to the specified output path.
    """
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {output_path}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

def unzip_file(zip_path):
    """
    Unzips the inner file to the current directory.
    """
    cwd = os.getcwd()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cwd)
    print(f"Unzipped: {zip_path} to current directory")

    # Edit the name of the extracted folder
    extracted_folder = os.path.join(cwd, "Cozy-Coding-Hour-Transcripts-main")
    if os.path.exists(extracted_folder):
        new_folder_name = "Cozy-Coding-Hour-Transcripts"
        os.rename(extracted_folder, os.path.join(cwd, new_folder_name))
        print(f"Renamed extracted folder to: {new_folder_name}")

    # Remove the zip file after extraction
    os.remove(zip_path)
    print(f"Removed zip file: {zip_path}")

if __name__ == "__main__":
    # URL of the Cozy Coding Hour Transcripts GitHub repository zip file
    url = "https://github.com/willtheorangeguy/Cozy-Coding-Hour-Transcripts/archive/refs/heads/main.zip"
    output_zip = "cozy_coding_hour_transcripts.zip"

    download_file(url, output_zip)
    unzip_file(output_zip)
