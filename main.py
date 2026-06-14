"""
Main script to run a series of Python scripts in order.
This script takes a year as an argument and runs each script sequentially.
"""

import sys
import subprocess

# List of numbered scripts in order
scripts = [
    '1_download.py',
    '2_converter.py',
    '3_tagger.py',
    '4_transcriber.py',
    '5_summarizer.py',
    '6_cleanup.py',
]

# List of years
years = [
    "2025",
    "2026"
]

def main():
    """Main function to run the scripts in order."""
    for year in years:
        for script in scripts:
            print(f"Running {script} for year {year}...")
            result = subprocess.run([sys.executable, script, year], check=False)
            if result.returncode != 0:
                print(f"Error: {script} failed with exit code {result.returncode}")
                sys.exit(result.returncode)
    print("All scripts completed successfully.")

if __name__ == "__main__":
    main()
