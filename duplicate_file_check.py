import os
from tqdm import tqdm

# Configuration
DIRECTORY = input("Enter the directory path to scan for duplicates: ")  # Allow dynamic directory input
OUTPUT_FILE = "duplicate_file_names_report.txt"

# Walk through the directory and gather file names and their paths
def gather_files_by_name(directory):
    """Collect all files by their names and store paths."""
    file_names = {}  # Store name -> list of full paths

    for root, _, files in os.walk(directory):
        for file in tqdm(files, desc="Scanning files"):
            full_path = os.path.join(root, file)

            if file in file_names:
                file_names[file].append(full_path)
            else:
                file_names[file] = [full_path]

    return file_names

# Identify duplicates based on file names
def find_name_duplicates(file_names):
    """Find duplicate file names."""
    duplicates = []

    for paths in file_names.values():
        if len(paths) > 1:  # More than one occurrence
            original = paths[0]
            duplicate_list = paths[1:]
            duplicates.append((original, duplicate_list))

    return duplicates

# Save duplicate file names to a text file with improved formatting
def save_report(duplicates):
    """Write duplicate file names to a text file in a readable format."""
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:  # Set encoding to UTF-8
            for original, duplicate_list in duplicates:
                f.write(f"Original file:  {original}\n")
                for duplicate in duplicate_list:
                    f.write(f"Duplicate found: {duplicate}\n")
                f.write("\n")  # Add an empty line between groups
        print(f"Duplicate file names report saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"An error occurred while saving the report: {e}")

# Main script logic
def main():
    try:
        print(f"Scanning directory: {DIRECTORY}")
        file_names = gather_files_by_name(DIRECTORY)

        print("Searching for duplicate file names...")
        duplicates = find_name_duplicates(file_names)

        print("Saving report...")
        save_report(duplicates)

        print("Process completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
