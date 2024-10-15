# Duplicate-File-Name-Checker
A lightweight Python tool that identifies files with the same name, and generate a clear and easy-to-read report.
It helps you locate duplicate files on your NAS or other drives without deleting any files automatically, ensuring that your data remains safe.

# Features
- Scans a directory (and all subdirectories) for duplicate file names.
- Outputs a readable report listing the original file and duplicate instances.
- Handles non-ASCII characters with UTF-8 encoding to avoid encoding errors.
- Allows dynamic input for directory paths during runtime.

# Requirements
- Python 3.x installed on your machine.
- The tqdm library for progress bars.
  You can install tqdm via:
```
pip install tqdm
```

# How to Use
1. Run the Script
Open a terminal or command prompt and navigate to the directory where the script is located.
Use the following command to run the script: python duplicate_file_check.py

2. Enter Directory Path
When prompted, enter the path of the directory you want to scan.

For example:
```
C:\Users\John\Documents\
```
3. View the Report
After the scan completes, a report named "duplicate_file_names_report.txt" will be saved in the same directory as the script.

# Report Format
The report will list the original file followed by duplicate files in a clear and readable format. 

Example:
```
Original file:  C:\Users\John\Documents\Work\ProjectA\report_final.docx
Duplicate found: C:\Users\John\Desktop\report_final.docx

Original file:  C:\Pictures\Vacation2023\IMG_001.jpg
Duplicate found: C:\Backup\OldPictures\IMG_001.jpg
Duplicate found: C:\Dropbox\Photos\IMG_001.jpg

Original file:  C:\Music\Albums\Artist\AlbumName\song1.mp3
Duplicate found: C:\Downloads\Music\song1.mp3
```

# License
This project is open source and free to use under the MIT License.

# Contributing
Feel free to submit issues or pull requests to improve the script!

Let me know if you need any other tweaks or improvements!
